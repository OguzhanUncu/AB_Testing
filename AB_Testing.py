import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

con = pd.read_excel("ab_testing.xlsx",sheet_name="Control Group")
test = pd.read_excel("ab_testing.xlsx",sheet_name="Test Group")
con.head()
test.head()

con.describe().T
test.describe().T
con["Purchase"].mean()  # 550.89
test["Purchase"].mean() # 582.10
# anlamlı bir farklılık var mı?

# p-value <  0.05 HO Reddedilir
# p-value <  0.05 H0 Reddedilemez

#Kontrol edilmesi gereken varsayımlar
#1-Normallik varsayımı
#2 2-homojenlik varsayımı

# Normallik varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: sağlanmamaktadır.

test_stat, pvalue = shapiro(con["Purchase"])
print(test_stat,pvalue)  # pvalue = 0.5891 sağlanmaktadır

test_stat, pvalue = shapiro(test["Purchase"])
print(test_stat,pvalue)  # pvalue = 0.154135 sağlanmaktadır.

# Varyansların homojenlik varsayımı
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(con["Purchase"],
                           test["Purchase"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# 0.1083 varyanslar homojendir.

# şimdi t testi yapabiliriz

# HO: Anlamlı bir farklılık yoktur
# H1: Vardır

test_stat, pvalue = ttest_ind(con["Purchase"],test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#  0.3493 anlamlı bir farklılık yoktur


# Hangi testler kullanıldı:
# Normallik varsayımı için shapiro testi, varyans varsayımı için levene, anlamlı bir farklılık olup olmadığını ölçmek için
# t-testini kullandık.



# anlamlı bir farklılık yoktur sonucuna ulaştık böylece, iki opsiyondan hangisini uygulamak bize kalmış
# bunun için biraz verilere bakalım

def toplamlar(dataframe):
    print("Kontrol Verisi:")
    for col in dataframe.columns:
        print(" {} toplam = {}".format(col,round(dataframe[col].sum())))
        print("*************************************************")

toplamlar(con)
toplamlar(test)

# sadece satın alımlar üzerin den baktık diğer değişkenlerinde analiz edilmesi gerekiyor

# EARNİNG
# normallik analizi

test_stat, pvalue = shapiro(con["Earning"])
print(test_stat,pvalue)  # normaldir

test_stat, pvalue = shapiro(test["Earning"])
print(test_stat,pvalue)  # normaldir

# Varyansların homojenlik varsayımı
test_stat, pvalue = levene(con["Earning"],
                           test["Earning"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue)) # homojendir

# t testi

test_stat, pvalue = ttest_ind(con["Earning"],test["Earning"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# iki kazanç arasında anlamlı bir farklılık vardır


# IMPRESSİON

# Normallik varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: sağlanmamaktadır.


test_stat, pvalue = shapiro(con["Impression"])
print(test_stat,pvalue)  # normal

test_stat, pvalue = shapiro(test["Impression"])
print(test_stat,pvalue)  # normal


# Varyansların homojenlik varsayımı
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(con["Impression"],
                           test["Impression"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue)) # normal

# HO: Anlamlı bir farklılık yoktur
# H1: Vardır

test_stat, pvalue = ttest_ind(con["Impression"],test["Impression"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

## CLICK

test_stat, pvalue = shapiro(con["Click"])
print(test_stat,pvalue)  # normal

test_stat, pvalue = shapiro(test["Click"])
print(test_stat,pvalue)  # normal

test_stat, pvalue = levene(con["Click"],
                           test["Click"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#varyans varsayımı sağlanmadı

test_stat, pvalue = mannwhitneyu(con["Click"],
                                 test["Click"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

####################### ORAN OLARAK TEST EDİLMESİ ##################################

# Son olarak görülme ve tıklanma arasındaki oransal farka bakıp karar verebiliriz
# H0: İki oran arasında ist ol an fark yoktur
# H1: vardır.

basari_sayisi = np.array([158701, 204026])
gozlem_sayilari = np.array([4820496, 4068457])
test_stat, pvalue = proportions_ztest(count=basari_sayisi, nobs=gozlem_sayilari)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Pvalue = 0.00
# vardır
