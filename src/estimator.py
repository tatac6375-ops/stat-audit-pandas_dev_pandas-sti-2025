# estimator module
import numpy as np
from scipy.stats import beta


def mle_bernoulli(data):
    """
    Maximum Likelihood Estimation (MLE) for Bernoulli distribution.

    Formula:
        theta_hat = k / n

    where:
        k = number of successes
        n = total observations

    Reference:
        Tsun (2020), Bernoulli MLE, p. xx
    """

    n = len(data)
    k = np.sum(data)

    theta_hat = k / n

    return {
        "theta_hat": theta_hat,
        "k": k,
        "n": n
    }


def mle_poisson(data):
    """
    Maximum Likelihood Estimation (MLE) for Poisson distribution.

    Formula:
        lambda_hat = mean(data)

    Reference:
        Tsun (2020), Poisson MLE, p. xx
    """

    lambda_hat = np.mean(data)

    return {
        "lambda_hat": lambda_hat
    }


def beta_posterior(k, n, alpha=1, beta_prior=1):
    """
    Beta posterior update for Bernoulli likelihood.

    Posterior:
        Beta(alpha + k, beta + n - k)

    Reference:
        Tsun (2020), Bayesian Estimation, p. xx
    """

    alpha_post = alpha + k
    beta_post = beta_prior + (n - k)

    posterior_mean = alpha_post / (alpha_post + beta_post)

    mode = (
        (alpha_post - 1) / (alpha_post + beta_post - 2)
        if alpha_post > 1 and beta_post > 1
        else None
    )

    return {
        "alpha": alpha_post,
        "beta": beta_post,
        "mean": posterior_mean,
        "mode": mode
    }


def log_likelihood_bernoulli(theta, k, n):
    """
    Log-likelihood for Bernoulli distribution.

    Formula:
        l(theta) = k log(theta) + (n-k) log(1-theta)

    Reference:
        Tsun (2020), Likelihood Theory, p. xx
    """

    return k * np.log(theta) + (n - k) * np.log(1 - theta)


def log_likelihood_poisson(theta, data):
    """
    Log-likelihood for Poisson distribution.

    Reference:
        Tsun (2020), Poisson Likelihood, p. xx
    """

    data = np.array(data)

    return np.sum(data * np.log(theta) - theta)