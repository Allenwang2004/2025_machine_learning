### Questions
1. There are more than one activation function, how to decide which one to use?
    For this question, I know that since sigmoid's derivative is smaller than 0.25, so if the netwrok is deep. It will cause Gradient Vanish. This is the reason why we will choose Relu if we train deep networks. But in gernel, I think there is a way for us to check whether the activation function is proper for the question condition.
2. If we use neural network, we can approximating any function. But if we want to use polynomial regression, how to decide which feature should be high-order?
3. In class, we talked about how many neurons are needed to approximate different powers of X. If the function being approximated is a multi-power term, does the number of neurons needed   to approximate it add up or is it completely irrelevant?
4. Since we cannot guarantee that each layer or each neuron in the neural network will learn a specific 
monomial individually, How can we say that the neural network can approximate any continuous function?
5. Gaussian Discriminant Analysis (GDA) assumes that the class-conditional distributions of the features are multivariate Gaussian. However, in many real-world datasets, this assumption is often violated. What are the standard techniques or model extensions to handle non-Gaussian feature distributions in generative classification frameworks
6. Does a multivariate Gaussian appear as a univariate Gaussian when sliced ​​out in each dimension?
7. Is the score function only used for continuous probability distributions in gernerative model?
8. If QDA’s decision boundary is roughly oval-shaped, what model can I use to capture more complex or highly curved boundaries?
9. How is the probability density function defined in high-dimensional spaces?
10.  It is possible to replace the Brownian motion in SDE to others, like jump diffusion?
    

### Answers
1. Datta et al., A Survey on Activation Functions and their relation with Deep Learning (2020). https://arxiv.org/pdf/2004.06632
2. Already have solution in scikit-learn : scikit-learn PolynomialFeatures documentation (standard implementation). https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
3. Barron, Universal Approximation Bounds for Superpositions of a Sigmoidal Function https://pages.cs.wisc.edu/~brecht/cs838docs/93.Barron.Universal.pdf
4. Cybenko, Approximation by Superpositions of a Sigmoidal Function https://web.njit.edu/~usman/courses/cs675_fall18/10.1.1.441.7873.pdf
5. Cinzia Viroli, Geoffrey J. McLachlan Deep Gaussian Mixture Models https://arxiv.org/abs/1711.06929
6. Course's note : https://bookdown.org/peter_neal/math4081-lectures/MV_Normal.html
7. C. Meng, K. Choi, J. Song, S. Ermon. “Concrete Score Matching: Generalized Score Matching for Discrete Data”. https://arxiv.org/abs/2211.00802
8. Hastie, Tibshirani: Flexible Discriminant and Mixture Models.  https://www.researchgate.net/publication/2445717_Flexible_Discriminant_and_Mixture_Models
9. Van Handel, Probability in High Dimension https://web.math.princeton.edu/~rvan/APC550.pdf
10. EUN BI YOON, Keehun Park, Sungwoong Kim, Sungbin Lim https://proceedings.neurips.cc/paper_files/paper/2023/file/8011b23e1dc3f57e1b6211ccad498919-Paper-Conference.pdf