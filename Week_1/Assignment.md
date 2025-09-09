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
\theta^{n+1} = \theta^n - \alpha\nabla_{\theta}\text{Loss}
$$
by the chain rule
$$
\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w_1}
$$
which
$$
z = b + w_1x_1 + w_2x_2
$$
so we have
$$
\frac{\partial L}{\partial w_1} = (\hat{y} - y) \cdot \hat{y}(1 - \hat{y}) \cdot x_1 = ( \sigma(21) - 3) \cdot \sigma(21)(1 - \sigma(21)) \cdot 1
$$
$$
\frac{\partial L}{\partial w_2} = (\hat{y} - y) \cdot \hat{y}(1 - \hat{y}) \cdot x_2 = (\sigma(21) - y) \cdot \sigma(21)(1 - \sigma(21)) \cdot 2
$$
$$
\frac{\partial L}{\partial b} = (\hat{y} - y) \cdot \hat{y}(1 - \hat{y}) \cdot 1  = (\sigma(21) - y) \cdot \sigma(21)(1 - \sigma(21)) \cdot 1
$$
therefore the answer is 
$$
\theta^1 =
\begin{bmatrix}
4 \\
5 \\
6 \\
\end{bmatrix}
-
\alpha \cdot (\sigma(21) - 3)\cdot \sigma(21)(1 - \sigma(21) \cdot
\begin{bmatrix}
1 \\
1 \\
2 \\
\end{bmatrix}
$$
---
### Question 2
(a)
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
f’’’(x) &= \frac{d}{dx} \left[ f’(x)(1 - 2f(x)) \right] \\
&= f’’(x)(1 - 2f(x)) + f’(x) \cdot \frac{d}{dx}(1 - 2f(x)) \\
&= f’’(x)(1 - 2f(x)) + f’(x)(-2f’(x)) \\
&= f’’(x)(1 - 2f(x)) - 2f’(x)^2 \\
&= f(x)(1 - f(x))(1 - 2f(x))(1 - 2f(x)) - 2 \cdot [f(x)(1 - f(x))]^2
\end{aligned}
$$
(b)
$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$
so
$$
\tanh(x) = 2\sigma(2x) - 1
$$
and
$$
\sigma(x) = \frac{1 + \tanh(x/2)}{2}
$$
---
