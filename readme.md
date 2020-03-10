![alt text](./images/portada.png "Que la generación Z no rompa tus modelos")

## Project description
The general purpose examples, included in the root path of this repo, are using the [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset. 
In this notebooks you will find some tests using explainability methods implemented in Python:
- [Activation Layers](https://raghakot.github.io/keras-vis/vis.visualization/#visualize_activation): Generates the model input that maximizes the output of all filter_indices in the given layer_idx
- [Saliency](https://raghakot.github.io/keras-vis/vis.visualization/#visualize_saliency): Generates an attention heatmap over the seed_input for maximizing filter_indices output in the given layer_idx
- [Grad Cam](https://raghakot.github.io/keras-vis/vis.visualization/#visualize_cam): Generates a gradient based class activation map (grad-CAM) that maximizes the outputs of filter_indices in layer_idx
- [Shap Gradient Explainer](https://shap.readthedocs.io/en/latest/#shap.GradientExplainer): Explains a model using expected gradients, an extension of the integrated gradients method (Sundararajan et al. 2017), a feature attribution method designed for differentiable models based on an extension of Shapley values to infinite player games (Aumann-Shapley values)
- [Lime Image Explainer](https://lime-ml.readthedocs.io/en/latest/lime.html#lime.lime_image.LimeImageExplainer): Explains predictions on Image (i.e. matrix) data. For numerical features, perturb them by sampling from a Normal(0,1) and doing the inverse operation of mean-centering and scaling, according to the means and stds in the training data. For categorical features, perturb by sampling according to the training distribution, and making a binary feature that is 1 when the value is the same as the instance being explained.

In the folder [stylesage-notebooks](/stylesage-notebooks) you will find some experiments using real data at [StyleSage.co](http://stylesage.co), the company where I work now. This notebooks will not work in your local environment as the images and trained models are not available, but you can see the code and results of your experiments. 

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
