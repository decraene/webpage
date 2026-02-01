Title: Deploy a static site to AWS with S3 and CloudFront
Date: 2026-01-03.
Summary:

Navigating the AWS console is always a challenge. 
To host this webpage, I'm using 3 very basic services: s3 for storing all files (```.html```, ```.css```, ```.png```, etc.), Route53 to handle DNS records, and CloudFront to cache and serve the content of the bucket. This makes a very efficient solution, that does not require to maintain any virtual machine, but combining all theses services was not that intuitive. Hopefully this tutorial can be of help!

### S3 Console

As for the bucket creation, things are simple here!

- Create bucket with default options
- Upload all files to your bucket (I recommend using the ```aws cli``` for this). 

```#bash
aws s3 sync my_local_folder s3://my_bucket_name
```

### CloudFront Console

This part is the most tricky one. Although it seems AWS has somehow made this easier by automatically updating the bucket access rights when following these steps. 

First, create a distribution, keeping it close the default settings. 

- Step1 Choose a plan: Select pay as you go 
- Step 2 
    - Choose _Distribution name_
    - Keep _Single website or app_ for distribution type
- Step 3 
    - Origin Type: _Amazon s3_
    - S3 Origin: Select your bucket there
    - Settings: keep recommended origin settings 
    - Keep recommended cache settings 
- Step 4: (De)activate WAF as per your needs
- Step 5: Review and create distribution

Then, in the newly created distribution, tune the following settings. In the first tab:

- Add a domain. Add your domain here, will be something like www.my-domain.com
- Use certificate if available or create a new one. 
- Review changes and click _Add domains_. 
- __Important__: Do not forget to add a default root object: in the generic settings, hit Modify then write _index.html_ 
(or other depending on your case) under _Default root object_. If you omit to do that, your users will have to navigate to www.my-domain.com/index.html as www.my-domain.com will return an error. 


### Route53 Console

Follow these steps:

- Add a record
- Define simple record
- Enter your subdomain (e.g. www)
- Type A
- Select _Alias to CloudFront distribution_
- In the search box, look for your cloud front distribution, and select it. 
- Hit the Create button.

Go to ```www.my-domain.com``` and cross your fingers. Hopefully you will see the content you uploaded to your bucket!

