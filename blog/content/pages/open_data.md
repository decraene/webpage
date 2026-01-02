Title: Open Data
Date: 2025-08-01.

During my early days at Philips, I was involved in a collaboration between Industry and Academia to validate the quantification of cardiac motion and deformation images, mostly from 3D ultrasound images.

This resulted in the following public datasets.

### cMAC challenge data

This data was used for the first Cardiac Motion Analysis Challenge, held at the 2011 MICCAI workshop entitled "Statistical Atlases and Computational Models of the Heart: Imaging an Modelling Challenges" ([STACOM 11]("https://stacom.github.io/").

The data includes MR and ultrasound images of 15 healthy volunteers in MR (including SSP and 4D tagged MR)
and 3D ultrasound (apical view).

The data is hosted on the [cardiac atlas platform](https://www.cardiacatlas.org/motion-tracking-2011-challenge/).

Get a copy of the paper describing the challenge and the dataset [here](https://inria.hal.science/hal-00855928/file/tobon-gomez12a_v2.0.pdf).

### 3D Straus data

The Straus acronym stands for "Strain assessment in ultrasound".
Initially, Straus was a collaboration between 3 partners:

- [Philips France](https://www.welcometothejungle.com/en/companies/philipshealthtechnologyinnovationparis/medisys)
- [KU Leuven](https://www.kuleuven.be/english/kuleuven)
- [Inria](https://team.inria.fr/epione/en/)

At the [STACOM 12](https://stacom.github.io/) MICCAI workshop, we released a dataset of synthetic 3D ultrasound images to validate 3D speckle tracking methods. 

As the original data URL is no longer available, a copy of the dataset can be found at this link: [https://straus.decraene.org](https://straus.decraene.org).

The paper describing the dataset and the challenge can be downloaded from [this HAL link](https://inria.hal.science/hal-00840039/document).


### 3D synthetic multimodal cardiac data

In a collaboration with [Creatis](https://humanheart-project.creatis.insa-lyon.fr/databases.html), we improved the realism of the 3D Straus data by combining real images with synthetic motion fields and advanced ultrasound and MR modeling techniques.

- The resulting multimodal dataset can be downloaded from the [Creatis Human Heart Project webpage](https://humanheart-project.creatis.insa-lyon.fr/database/#collection/587de6f4e1af3f30a2980a58).
- The ultrasound part of the dataset can be downloaded from [here](https://www-sop.inria.fr/asclepios/data/STRAUS/).
- See [this page](https://team.inria.fr/epione/en/data/straus/) for further details.
- See [this paper](https://lirias.kuleuven.be/retrieve/300334") for a description of the ultrasound modeling pipeline.
- See [this other paper](https://inria.hal.science/hal-01533366/document) for the extension to MR and ultrasound.


### CAMUS synthetic database</h3>
As a 2D version of the Straus data, we released a synthetic 2D dataset for training DL-based image tracking algorithms.

- The data is available on the [Human Heart Project webpage](https://humanheart-project.creatis.insa-lyon.fr/database/#collection/61c250d873e9f0047c37d62f).
- Get a copy of the paper [here](https://hal.science/hal-03603014/document).