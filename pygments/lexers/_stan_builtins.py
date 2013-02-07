# -*- coding: utf-8 -*-
"""
    pygments.lexers._stan_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This file contains the names of functions for Stan used by
    ``pygments.lexers.math.StanLexer.

    :copyright: Copyright 2006-2013 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

CONSTANTS = [   'e',
    'epsilon',
    'log10',
    'log2',
    'negative_epsilon',
    'negative_infinity',
    'not_a_number',
    'pi',
    'positive_infinity',
    'sqrt2']

FUNCTIONS = [   'Phi',
    'abs',
    'acos',
    'acosh',
    'asin',
    'asinh',
    'atan',
    'atan2',
    'atanh',
    'bernoulli_log',
    'beta_binomial_log',
    'beta_log',
    'binary_log_loss',
    'binomial_coefficient_log',
    'block',
    'categorical_log',
    'cauchy_log',
    'cbrt',
    'ceil',
    'chi_square_log',
    'cholesky_decompose',
    'col',
    'cols',
    'cos',
    'cosh',
    'cumulative_sum',
    'determinant',
    'diag_matrix',
    'diagonal',
    'dirichlet_log',
    'dot_product',
    'dot_self',
    'double_exponential_log',
    'eigenvalues',
    'eigenvalues_sym',
    'erf',
    'erfc',
    'exp',
    'exp2',
    'expm1',
    'exponential_cdf',
    'exponential_log',
    'fabs',
    'fdim',
    'floor',
    'fma',
    'fmax',
    'fmin',
    'fmod',
    'gamma_log',
    'hypergeometric_log',
    'hypot',
    'if_else',
    'int_step',
    'inv_chi_square_log',
    'inv_cloglog',
    'inv_gamma_log',
    'inv_logit',
    'inv_wishart_log',
    'inverse',
    'lbeta',
    'lgamma',
    'lkj_corr_cholesky_log',
    'lkj_corr_log',
    'lkj_cov_log',
    'lmgamma',
    'log',
    'log10',
    'log1m',
    'log1p',
    'log1p_exp',
    'log2',
    'log_inv_logit',
    'log1m_inv_logit',
    'log_sum_exp',
    'logistic_log',
    'logit',
    'lognormal_cdf',
    'lognormal_log',
    'max',
    'mdivide_left_tri_low',
    'mdivide_right_tri_low',
    'mean',
    'min',
    'multi_normal_cholesky_log',
    'multi_normal_log',
    'multi_student_t_log',
    'multinomial_log',
    'multiply_log',
    'multiply_lower_tri_self_transpose',
    'neg_binomial_log',
    'normal_cdf',
    'normal_log',
    'ordered_logistic_log',
    'pareto_log',
    'poisson_log',
    'poisson_log_log',
    'pow',
    'prod',
    'round',
    'row',
    'rows',
    'scaled_inv_chi_square_log',
    'sd',
    'sin',
    'singular_values',
    'sinh',
    'softmax',
    'sqrt',
    'square',
    'step',
    'student_t_log',
    'sum',
    'tan',
    'tanh',
    'tgamma',
    'trace',
    'trunc',
    'uniform_log',
    'variance',
    'weibull_cdf',
    'weibull_log',
    'wishart_log']

DISTRIBUTIONS = [   'bernoulli',
    'beta',
    'beta_binomial',
    'categorical',
    'cauchy',
    'chi_square',
    'dirichlet',
    'double_exponential',
    'exponential',
    'gamma',
    'hypergeometric',
    'inv_chi_square',
    'inv_gamma',
    'inv_wishart',
    'lkj_corr',
    'lkj_corr_cholesky',
    'lkj_cov',
    'logistic',
    'lognormal',
    'multi_normal',
    'multi_normal_cholesky',
    'multi_student_t',
    'multinomial',
    'neg_binomial',
    'normal',
    'ordered_logistic',
    'pareto',
    'poisson',
    'poisson_log',
    'scaled_inv_chi_square',
    'student_t',
    'uniform',
    'weibull',
    'wishart']

CPP_RESERVED = [
    'alignas',
    'alignof',
    'and',
    'and_eq',
    'asm',
    'auto',
    'bitand',
    'bitor'
    'bool',
    'break',
    'case',
    'catch',
    'char',
    'char16_t',
    'char32_t',
    'class'
    'compl',
    'const',
    'constexpr',
    'const_cast',
    'continue',
    'decltype'
    'default',
    'delete',
    'do',
    'double',
    'dynamic_cast',
    'else',
    'enum'
    'explicit',
    'export',
    'extern',
    'false',
    'float',
    'for',
    'friend',
    'goto'
    'if',
    'inline',
    'int',
    'long',
    'mutable',
    'namespace',
    'new',
    'noexcept'
    'not',
    'not_eq',
    'nullptr',
    'operator',
    'or',
    'or_eq',
    'private',
    'protected'
    'public',
    'register',
    'reinterpret_cast',
    'return',
    'short',
    'signed'
    'sizeof',
    'static',
    'static_assert',
    'static_cast',
    'struct',
    'switch'
    'template',
    'this',
    'thread_local',
    'throw',
    'true',
    'try',
    'typedef'
    'typeid',
    'typename',
    'union',
    'unsigned',
    'using',
    'virtual',
    'void'
    'volatile',
    'wchar_t',
    'while',
    'xor',
    'xor_eq'
    ]
