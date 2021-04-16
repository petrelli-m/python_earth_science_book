def returns_normal_tests(my_data):
    
    from scipy.stats import shapiro, anderson, normaltest

    print('---------------------------------------------')
    print('')
    stat, p = shapiro(my_data)
    alpha = 0.05
    if p > alpha:
    	print('Shapiro test fails to reject H0: looks normal :)')
    else:
    	print('Shapiro test rejects H0: not normal :(')
    print('')
    stat, p = normaltest(my_data)
    alpha = 0.05
    if p > alpha:
    	print("D%*\textcolor{codered}{$\textquotesingle$}*)Agostino and Pearson%*\textcolor{codered}{$\textquotesingle$}*)s test fails to reject H0: looks normal :)")
    else:
    	print("D%*\textcolor{codered}{$\textquotesingle$}*)Agostino and Pearson%*\textcolor{codered}{$\textquotesingle$}*)s test rejects H0: not normal :(")
    print('')    
    result = anderson(my_data)
    print('Anderson-Darling test:')
    for sl, cv in zip(result.significance_level, result.critical_values):
    	if result.statistic < cv:
    		print('%.3f: fails to reject H0: Sample looks normal :)' % (sl))
    	else:
    		print('%.3f: rejects H0: Sample does not look normal :(' % (sl))
    print('---------------------------------------------')
    print('')

# Original MnO sample
print('Original MnO sample')
returns_normal_tests(MnO)

# Removing the outliers above 0.27 wt %
print('MnO sample without observations above 0.27 wt %')
MnO_no_outliers = MnO[MnO < 0.27]
returns_normal_tests(MnO_no_outliers)

''' Results:
Original MnO sample
---------------------------------------------

Shapiro test rejects H0: not normal :(

D%*\textcolor{codegreen}{$\textquotesingle$}*)Agostino and Pearson%*\textcolor{codegreen}{$\textquotesingle$}*)s test rejects H0: not normal :(

Anderson-Darling test:
15.000: rejects H0: Sample does not look normal :(
10.000: rejects H0: Sample does not look normal :(
5.000: rejects H0: Sample does not look normal :(
2.500: rejects H0: Sample does not look normal :(
1.000: rejects H0: Sample does not look normal :(
---------------------------------------------

MnO sample without observations above 0.27 wt %
---------------------------------------------

Shapiro test fails to reject H0: looks normal :)

D%*\textcolor{codegreen}{$\textquotesingle$}*)Agostino and Pearson%*\textcolor{codegreen}{$\textquotesingle$}*)s test fails to reject H0: looks normal :)

Anderson-Darling test:
15.000: fails to reject H0: Sample looks normal :)
10.000: fails to reject H0: Sample looks normal :)
5.000: fails to reject H0: Sample looks normal :)
2.500: fails to reject H0: Sample looks normal :)
1.000: fails to reject H0: Sample looks normal :)
-----------------------------------------------------------
'''