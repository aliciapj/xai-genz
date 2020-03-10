![alt text](./images/portada.png "Que la generación Z no rompa tus modelos")

This repo contains the resources used in the talk "Que la generación Z no rompa tus modelos":
- 2019-10-05: [PyConEs Alicante](https://pycones19.sched.com/event/VdMa/que-la-generacion-z-no-rompa-tus-modelos) | [Slides](https://static.sched.com/hosted_files/pycones19/d0/PyCon2019%20-%20Fairness_Bias.pdf) - [Video](https://www.youtube.com/watch?v=Kq2pk99OD90)
- 2020-xx-xx: T3chFest Madrid | Slides soon

### Alphanumeric data sets
* [Adult Census Income](/adult-census-income): This data was extracted from the 1994 Census bureau database by Ronny Kohavi and Barry Becker (Data Mining and Visualization, Silicon Graphics). A set of reasonably clean records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1) && (HRSWK>0)). The prediction task is to determine whether a person makes over $50K a year. More info [here](https://www.kaggle.com/uciml/adult-census-income)
* [Compass vs Prodata](/compas-propublica): COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) is a popular commercial algorithm used by judges and parole officers for scoring criminal defendant’s likelihood of reoffending (recidivism). It has been shown that the algorithm is biased in favor of white defendants, and against black inmates, based on a 2 year follow up study (i.e who actually committed crimes or violent crimes after 2 years). The pattern of mistakes, as measured by precision/sensitivity is notable. More info [here](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
* [German Credit Scoring](/german-credit-scoring): The original dataset contains 1000 entries with 20 categorial/symbolic attributes prepared by Prof. Hofmann. In this dataset, each entry represents a person who takes a credit by a bank. Each person is classified as good or bad credit risks according to the set of attributes. The link to the original dataset can be found below. More info [here](https://www.kaggle.com/uciml/german-credit#german_credit_data.csv)
* [USA Presidential election](/usa_presidential_election_data): These data files contain election results for both the 2012 and 2016 US Presidential Elections, include proportions of votes cast for Romney, Obama (2012) and Trump, Clinton (2016). More info [here](https://www.kaggle.com/joelwilson/2012-2016-presidential-elections/)


The XAI methods used in these notebooks are the following:
* [Permutation importance](https://eli5.readthedocs.io/en/latest/blackbox/permutation_importance.html): Library eli5 provides a way to compute feature importances for any black-box estimator by measuring how score decreases when a feature is not available; the method is also known as “permutation importance” or “Mean Decrease Accuracy (MDA)”.
* [Partial Dependence Plots](https://www.kaggle.com/dansbecker/partial-dependence-plots): were introduced by Friedman (2001) with purpose of interpreting complex Machine Learning algorithms. Given a dataset D with n observations and p predictor variables and y as response variable. Partial Dependence Plot helps understand varaible important in a given model.
* [FairML](https://github.com/adebayoj/fairml): FairML is a python toolbox auditing the machine learning models for bias.
* [LIME](https://github.com/marcotcr/lime): Lime is able to explain any black box classifier, with two or more classes. All it require is that the classifier implements a function that takes in raw text or a numpy array and outputs a probability for each class. 
* [What-If Tool](https://pair-code.github.io/what-if-tool/): The What-If Tool (WIT) provides an easy-to-use interface for expanding understanding of a black-box classification or regression ML model. With the plugin, you can perform inference on a large set of examples and immediately visualize the results in a variety of ways. Additionally, examples can be edited manually or programmatically and re-run through the model in order to see the results of the changes. It contains tooling for investigating model performance and fairness over subsets of a dataset.


### Image based datasets

* [Fashion-MNIST](/fashion_mnist): is a dataset of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. We intend Fashion-MNIST to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits. More info [here](https://github.com/zalandoresearch/fashion-mnist): 
* [StyleSage Notebooks](/stylesage-notebooks): in this folder you will find some experiments using real data at [StyleSage.co](http://stylesage.co), the company where I work now. This notebooks will not work in your local environment as the images and trained models are not available, but you can see the code and results of your experiments. 


The XAI methods used in these notebooks are the following:
- [Activation Layers](https://raghakot.github.io/keras-vis/vis.visualization/#visualize_activation): Generates the model input that maximizes the output of all filter_indices in the given layer_idx
- [Saliency](https://raghakot.github.io/keras-vis/vis.visualization/#visualize_saliency): Generates an attention heatmap over the seed_input for maximizing filter_indices output in the given layer_idx
- [Grad Cam](https://raghakot.github.io/keras-vis/vis.visualization/#visualize_cam): Generates a gradient based class activation map (grad-CAM) that maximizes the outputs of filter_indices in layer_idx
- [Shap Gradient Explainer](https://shap.readthedocs.io/en/latest/#shap.GradientExplainer): Explains a model using expected gradients, an extension of the integrated gradients method (Sundararajan et al. 2017), a feature attribution method designed for differentiable models based on an extension of Shapley values to infinite player games (Aumann-Shapley values)
- [Lime Image Explainer](https://lime-ml.readthedocs.io/en/latest/lime.html#lime.lime_image.LimeImageExplainer): Explains predictions on Image (i.e. matrix) data. For numerical features, perturb them by sampling from a Normal(0,1) and doing the inverse operation of mean-centering and scaling, according to the means and stds in the training data. For categorical features, perturb by sampling according to the training distribution, and making a binary feature that is 1 when the value is the same as the instance being explained.

### Installation

This project was developed using Python 3.6.9;
> More info about Python installation [here](https://www.python.org/downloads/release/python-374/)

I recommend to use a virtual environment for the project. More info about it [here](https://docs.python.org/3/library/venv.html)
```bash
python3 -m venv /path/to/new/virtual/environment
```
You can install the required libraries using pip with the following command:
```
pip install -r requirements.txt
```
