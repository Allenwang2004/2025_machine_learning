### Question 1

Since the model is 
$$
h(x_1, x_2) = \sigma(b + w_1x_1 + w_2x_2)
$$
Put in the data and parameter, we got
$$
h(1, 2) = \sigma(4 + 5\cdot1 + 6\cdot2)=\sigma(21)
$$
And the Loss function is
$$
Loss(\theta) = \frac{1}{2}(h(x_1, x_2) - y)^2
$$
we have
$$
\theta^{n+1} = \theta^n - \alpha\nabla_{\theta}\text{Loss}, 
$$

### Question 2
For k = 1 
$$
\begin{aligned}
f’(x) &= \frac{d}{dx} \left( \frac{1}{1 + e^{-x}} \right) \\
&= \frac{d}{dx} \left( \frac{e^x}{e^x + 1} \right) \\
&= \frac{d}{dx} \left( 1 - (e^x + 1)^{\,-1} \right) \\
&= (-1)(-1)(1 + e^{-x})^{-2} \cdot e^{-x} \\
&= (1 + e^{-x})^{-2} \cdot e^{-x} \\
&= \left( \frac{1}{1 + e^{-x}} \right) \cdot \left( \frac{e^{-x}}{1 + e^{-x}} \right) \\
&= f(x)(1 - f(x))
\end{aligned}
$$

For k = 2
$$
\begin{aligned}
f’’(x) &= \frac{d}{dx} \left[ f(x)(1 - f(x)) \right] \\
&= f’(x)(1 - f(x)) - f(x) \cdot f’(x) \\
&= f’(x)[1 - f(x) - f(x)] \\
&= f’(x)(1 - 2f(x)) \\
&= f(x)(1 - f(x))(1 - 2f(x))
\end{aligned}
$$

For k = 3
$$
\begin{aligned}
f’’’(x) &= \frac{d}{dx} \left[ f(x)(1 - f(x))(1 - 2f(x)) \right] \\
&= f’’(x)(1 - 2f(x)) + f’(x) \cdot \frac{d}{dx}(1 - 2f(x)) \\
&= f’’(x)(1 - 2f(x)) + f’(x)(-2f’(x)) \\
&= f’’(x)(1 - 2f(x)) - 2f’(x)^2 \\
&= f(x)(1 - f(x))(1 - 2f(x))(1 - 2f(x)) - 2 \cdot [f(x)(1 - f(x))]^2
\end{aligned}
$$

### Question 3
1. There are more than one activation function, how to decide which one to use?
2. If we use neural network, we can approximating any function. But if we want to use polynomial regression, how to decide which feature should be high-order?