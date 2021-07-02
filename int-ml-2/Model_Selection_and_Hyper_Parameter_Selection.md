# Model Selection and Hyper-Parameters Selection

## Model Selection

**Model selection** is the process of selecting one *final machine learning model* from among a collection of candidate machine learning models for a training dataset.

*Model selection* is a process that can be applied both across different types of models (e.g. *logistic regression, SVM, KNN*, etc.) and across models of the same type configured with different model hyperparameters (e.g. *different kernels in an SVM*).

We evaluate or assess candidate models in order to choose the best one, and this is **model selection**. Whereas once a model is chosen, it can be evaluated in order to communicate how well it is expected to perform in general; this is **model assessment**.

A ***good enough*** model may refer to many things and is specific to your project, such as:

*	A model that meets the requirements and constraints of project stakeholders.
*	A model that is sufficiently skilful given the time and resources available.
*	A model that is skilful as compared to naive models.
*	A model that is skilful relative to other tested models.
*	A model that is skilful relative to the state-of-the-art.

The best approach to model selection requires ***sufficient*** data, which may be nearly infinite depending on the complexity of the problem.

In this ideal situation, we would split the data into *training*, *validation*, and *test* sets, then fit candidate models on the ***training*** set, evaluate and select them on the ***validation*** set, and report the performance of the final model on the ***test*** set.

***Probabilistic*** measures involve analytically scoring a candidate model using both its performance on the *training* dataset and the complexity of the model.

A model with fewer parameters is less complex, and because of this, is preferred because it is likely to generalize better on average.

## Hyper-Parameters Selection

A ***hyperparameter*** can be loosely defined as a parameter that is not tuned during the learning phase that optimizes the main objective function on the training set. While a simple grid search would yield the optimal hyperparameters by trying all possible combinations of hyper parameters, it does not scale as the number of hyperparameters and the data set size increase. As a result, investigators typically choose hyperparameters arbitrarily, after a series of manual trials, which can sometimes cast doubts on the results as investigators might have been tempted to tune the parameters specifically for the test set.

For example, the *tree depth* in a decision tree model and the *number of layers* in an artificial neural network are typical hyperparameters. The performance of a model can drastically depend on the choice of its hyperparameters. A decision tree can yield good results for moderate tree depth and have very bad performance for very deep trees.

There are basically four methods for choosing hyper-parameters:

1. **Manual Search**: Using knowledge you have about the problem guess parameters and observe the result. Based on that result tweak the parameters. Repeat this process until you find parameters that work well or you run out of time.

1. **Grid Search**: Using knowledge you have about the problem identify ranges for the hyperparameters. Then select several points from those ranges, usually uniformly distributed. Train your network using every combination of parameters and select the combination that performs best. Alternatively, you can repeat your search on a narrower domain centred around the parameters that perform the best.

1. **Random Search**: Like grid search you use knowledge of the problem to identify ranges for the hyperparameters. However instead of picking values from those ranges in a methodical manner you instead select them at random. Repeat this process until you find parameters that work well or use what you learn to narrow your search. In the paper Random Search for Hyper-Parameter Optimization Dr. Bengio proposes this be the baseline method against which all other methods should be compared and shows that it tends to work better than the other methods.

1. **Bayesian Optimization**: More recent work has been focussed on improving upon these other approaches by using the information gained from any given experiment to decide how to adjust the hyper parameters for the next experiment. An example of this work would be Practical Bayesian Optimization of Machine Learning Algorithms by Adams et al.
