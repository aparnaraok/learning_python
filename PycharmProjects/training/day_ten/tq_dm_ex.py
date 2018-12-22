#tqdm shows the progress bar of tranfer rate of large files
#Total Quality Data Management
from tqdm import tqdm
import sys
import time
import paramiko

def viewBar(a,b):

    #a - How much amount transferred
    #Total size is b

    print ("A is ", a)
    print ("B is ", b)
    res = a / int(b)*100
    sys.stdout.write('\rComplete Percent : %.2f %%' % (res))
    sys.stdout.flush()

def viewBar2(a, b):
    pbar = tqdm(total = int(b), ascii=False, unit='b', unit_scale=True)
    pbar.update(a)

    #unit .....bytes
    #if ASCII is false..shows graph

#Transport can be replaces by SSH client too
t = paramiko.Transport(('localhost', 22))
t.connect(username='cisco', password='cisco')

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('thebook.pdf', '/tmp/mlearn.pdf', callback=viewBar2)
#sftp.put('thebook.pdf', '/tmp/mlearn.pdf', callback=viewBar)
t.close()

#When ASCII is FALSE
# 99%|█████████▉| 10.7M/10.8M [00:00<00:00, 163Gb/s]
# 100%|█████████▉| 10.8M/10.8M [00:00<00:00, 77.0Gb/s]
# 100%|██████████| 10.8M/10.8M [00:00<00:00, 159Gb/s]

#WHEN ASCII is True
#   0%|          | 32.8k/10.8M [00:00<00:00, 179Mb/s]
#   1%|          | 65.5k/10.8M [00:00<00:00, 351Mb/s]
#   1%|          | 98.3k/10.8M [00:00<00:00, 696Mb/s]
#   1%|1         | 131k/10.8M [00:00<00:00, 1.07Gb/s]
#   2%|1         | 164k/10.8M [00:00<00:00, 1.64Gb/s]
#   2%|1         | 197k/10.8M [00:00<00:00, 1.85Gb/s]
#   2%|2         | 229k/10.8M [00:00<00:00, 2.07Gb/s]
#   2%|2         | 262k/10.8M [00:00<00:00, 2.41Gb/s]
#   3%|2         | 295k/10.8M [00:00<00:00, 2.78Gb/s]
#   3%|3         | 328k/10.8M [00:00<00:00, 3.30Gb/s]
#   3%|3         | 360k/10.8M [00:00<00:00, 3.81Gb/s]
#   4%|3         | 393k/10.8M [00:00<00:00, 3.71Gb/s]
#   4%|3         | 426k/10.8M [00:00<00:00, 4.31Gb/s]
#   4%|4         | 459k/10.8M [00:00<00:00, 4.96Gb/s]
#   5%|4         | 492k/10.8M [00:00<00:00, 5.17Gb/s]
#   5%|4         | 524k/10.8M [00:00<00:00, 5.38Gb/s]
#   5%|5         | 557k/10.8M [00:00<00:00, 6.23Gb/s]
#   5%|5         | 590k/10.8M [00:00<00:00, 5.90Gb/s]
#   6%|5         | 623k/10.8M [00:00<00:00, 5.91Gb/s]
#   6%|6         | 655k/10.8M [00:00<00:00, 6.69Gb/s]
#   6%|6         | 688k/10.8M [00:00<00:00, 3.52Gb/s]
#   7%|6         | 721k/10.8M [00:00<00:00, 9.48Gb/s]
#   7%|6         | 754k/10.8M [00:00<00:00, 9.82Gb/s]
#   7%|7         | 786k/10.8M [00:00<00:00, 9.59Gb/s]
#   8%|7         | 819k/10.8M [00:00<00:00, 2.67Gb/s]
#   8%|7         | 852k/10.8M [00:00<00:00, 12.1Gb/s]
#   8%|8         | 885k/10.8M [00:00<00:00, 4.51Gb/s]
#   8%|8         | 918k/10.8M [00:00<00:00, 12.5Gb/s]
#   9%|8         | 950k/10.8M [00:00<00:00, 13.5Gb/s]
#   9%|9         | 983k/10.8M [00:00<00:00, 8.35Gb/s]
#   9%|9         | 1.02M/10.8M [00:00<00:00, 12.8Gb/s]
#  10%|9         | 1.05M/10.8M [00:00<00:00, 886Mb/s]
#  10%|#         | 1.08M/10.8M [00:00<00:00, 12.2Gb/s]
#  10%|#         | 1.11M/10.8M [00:00<00:00, 8.97Gb/s]
#  11%|#         | 1.15M/10.8M [00:00<00:00, 14.7Gb/s]
#  11%|#         | 1.18M/10.8M [00:00<00:00, 13.5Gb/s]
#  11%|#1        | 1.21M/10.8M [00:00<00:00, 14.9Gb/s]
#  12%|#1        | 1.25M/10.8M [00:00<00:00, 5.60Gb/s]
#  12%|#1        | 1.28M/10.8M [00:00<00:00, 9.23Gb/s]
#  12%|#2        | 1.31M/10.8M [00:00<00:00, 16.4Gb/s]
#  12%|#2        | 1.34M/10.8M [00:00<00:00, 16.7Gb/s]
#  13%|#2        | 1.38M/10.8M [00:00<00:00, 15.2Gb/s]
#  13%|#3        | 1.41M/10.8M [00:00<00:00, 16.3Gb/s]
#  13%|#3        | 1.44M/10.8M [00:00<00:00, 18.9Gb/s]
#  14%|#3        | 1.47M/10.8M [00:00<00:00, 12.8Gb/s]
#  14%|#3        | 1.51M/10.8M [00:00<00:00, 3.71Gb/s]
#  14%|#4        | 1.54M/10.8M [00:00<00:00, 10.9Gb/s]
#  15%|#4        | 1.57M/10.8M [00:00<00:00, 16.5Gb/s]
#  15%|#4        | 1.61M/10.8M [00:00<00:00, 17.9Gb/s]
#  15%|#5        | 1.64M/10.8M [00:00<00:00, 21.8Gb/s]
#  15%|#5        | 1.67M/10.8M [00:00<00:00, 19.7Gb/s]
#  16%|#5        | 1.70M/10.8M [00:00<00:00, 21.8Gb/s]
#  16%|#6        | 1.74M/10.8M [00:00<00:00, 22.1Gb/s]
#  16%|#6        | 1.77M/10.8M [00:00<00:00, 20.6Gb/s]
#  17%|#6        | 1.80M/10.8M [00:00<00:00, 21.5Gb/s]
#  17%|#6        | 1.84M/10.8M [00:00<00:00, 22.2Gb/s]
#  17%|#7        | 1.87M/10.8M [00:00<00:00, 8.49Gb/s]
#  18%|#7        | 1.90M/10.8M [00:00<00:00, 4.58Gb/s]
#  18%|#7        | 1.93M/10.8M [00:00<00:00, 21.7Gb/s]
#  18%|#8        | 1.97M/10.8M [00:00<00:00, 15.0Gb/s]
#  18%|#8        | 2.00M/10.8M [00:00<00:00, 18.6Gb/s]
#  19%|#8        | 2.03M/10.8M [00:00<00:00, 15.2Gb/s]
#  19%|#9        | 2.06M/10.8M [00:00<00:00, 19.1Gb/s]
#  19%|#9        | 2.10M/10.8M [00:00<00:00, 10.4Gb/s]
#  20%|#9        | 2.13M/10.8M [00:00<00:00, 26.6Gb/s]
#  20%|##        | 2.16M/10.8M [00:00<00:00, 3.78Gb/s]
#  20%|##        | 2.20M/10.8M [00:00<00:00, 28.4Gb/s]
#  21%|##        | 2.23M/10.8M [00:00<00:00, 20.7Gb/s]
#  21%|##        | 2.26M/10.8M [00:00<00:00, 18.2Gb/s]
#  21%|##1       | 2.29M/10.8M [00:00<00:00, 16.2Gb/s]
#  22%|##1       | 2.33M/10.8M [00:00<00:00, 32.1Gb/s]
#  22%|##1       | 2.36M/10.8M [00:00<00:00, 23.4Gb/s]
#  22%|##2       | 2.39M/10.8M [00:00<00:00, 15.4Gb/s]
#  22%|##2       | 2.42M/10.8M [00:00<00:00, 33.5Gb/s]
#  23%|##2       | 2.46M/10.8M [00:00<00:00, 16.1Gb/s]
#  23%|##3       | 2.49M/10.8M [00:00<00:00, 31.4Gb/s]
#  23%|##3       | 2.52M/10.8M [00:00<00:00, 35.4Gb/s]
#  24%|##3       | 2.56M/10.8M [00:00<00:00, 35.5Gb/s]
#  24%|##3       | 2.59M/10.8M [00:00<00:00, 10.2Gb/s]
#  24%|##4       | 2.62M/10.8M [00:00<00:00, 35.5Gb/s]
#  25%|##4       | 2.65M/10.8M [00:00<00:00, 11.0Gb/s]
#  25%|##4       | 2.69M/10.8M [00:00<00:00, 33.1Gb/s]
#  25%|##5       | 2.72M/10.8M [00:00<00:00, 24.4Gb/s]
#  25%|##5       | 2.75M/10.8M [00:00<00:00, 6.84Gb/s]
#  26%|##5       | 2.79M/10.8M [00:00<00:00, 18.5Gb/s]
#  26%|##6       | 2.82M/10.8M [00:00<00:00, 34.4Gb/s]
#  26%|##6       | 2.85M/10.8M [00:00<00:00, 24.7Gb/s]
#  27%|##6       | 2.88M/10.8M [00:00<00:00, 25.8Gb/s]
#  27%|##6       | 2.92M/10.8M [00:00<00:00, 15.4Gb/s]
#  27%|##7       | 2.95M/10.8M [00:00<00:00, 29.0Gb/s]
#  28%|##7       | 2.98M/10.8M [00:00<00:00, 36.7Gb/s]
#  28%|##7       | 3.01M/10.8M [00:00<00:00, 38.8Gb/s]
#  28%|##8       | 3.05M/10.8M [00:00<00:00, 35.4Gb/s]
#  28%|##8       | 3.08M/10.8M [00:00<00:00, 39.4Gb/s]
#  29%|##8       | 3.11M/10.8M [00:00<00:00, 41.8Gb/s]
#  29%|##9       | 3.15M/10.8M [00:00<00:00, 6.50Gb/s]
#  29%|##9       | 3.18M/10.8M [00:00<00:00, 37.7Gb/s]
#  30%|##9       | 3.21M/10.8M [00:00<00:00, 44.3Gb/s]
#  30%|###       | 3.24M/10.8M [00:00<00:00, 29.6Gb/s]
#  30%|###       | 3.28M/10.8M [00:00<00:00, 43.2Gb/s]
#  31%|###       | 3.31M/10.8M [00:00<00:00, 27.7Gb/s]
#  31%|###       | 3.34M/10.8M [00:00<00:00, 33.6Gb/s]
#  31%|###1      | 3.38M/10.8M [00:00<00:00, 32.7Gb/s]
#  32%|###1      | 3.41M/10.8M [00:00<00:00, 32.3Gb/s]
#  32%|###1      | 3.44M/10.8M [00:00<00:00, 32.2Gb/s]
#  32%|###2      | 3.47M/10.8M [00:00<00:00, 29.2Gb/s]
#  32%|###2      | 3.51M/10.8M [00:00<00:00, 2.17Gb/s]
#  33%|###2      | 3.54M/10.8M [00:00<00:00, 6.55Gb/s]
#  33%|###3      | 3.57M/10.8M [00:00<00:00, 38.1Gb/s]
#  33%|###3      | 3.60M/10.8M [00:00<00:00, 28.9Gb/s]
#  34%|###3      | 3.64M/10.8M [00:00<00:00, 1.49Gb/s]
#  34%|###3      | 3.67M/10.8M [00:00<00:00, 2.84Gb/s]
#  34%|###4      | 3.70M/10.8M [00:00<00:00, 42.7Gb/s]
#  35%|###4      | 3.74M/10.8M [00:00<00:00, 43.9Gb/s]
#  35%|###4      | 3.77M/10.8M [00:00<00:00, 652Mb/s]
#  35%|###5      | 3.80M/10.8M [00:00<00:00, 31.0Gb/s]
#  35%|###5      | 3.83M/10.8M [00:00<00:00, 32.9Gb/s]
#  36%|###5      | 3.87M/10.8M [00:00<00:00, 33.1Gb/s]
#  36%|###6      | 3.90M/10.8M [00:00<00:00, 20.0Gb/s]
#  36%|###6      | 3.93M/10.8M [00:00<00:00, 12.4Gb/s]
#  37%|###6      | 3.96M/10.8M [00:00<00:00, 13.3Gb/s]
#  37%|###6      | 4.00M/10.8M [00:00<00:00, 24.9Gb/s]
#  37%|###7      | 4.03M/10.8M [00:00<00:00, 46.7Gb/s]
#  38%|###7      | 4.06M/10.8M [00:00<00:00, 51.2Gb/s]
#  38%|###7      | 4.10M/10.8M [00:00<00:00, 51.4Gb/s]
#  38%|###8      | 4.13M/10.8M [00:00<00:00, 36.6Gb/s]
#  38%|###8      | 4.16M/10.8M [00:00<00:00, 54.2Gb/s]
#  39%|###8      | 4.19M/10.8M [00:00<00:00, 54.6Gb/s]
#  39%|###9      | 4.23M/10.8M [00:00<00:00, 42.1Gb/s]
#  39%|###9      | 4.26M/10.8M [00:00<00:00, 53.7Gb/s]
#  40%|###9      | 4.29M/10.8M [00:00<00:00, 52.3Gb/s]
#  40%|####      | 4.33M/10.8M [00:00<00:00, 43.1Gb/s]
#  40%|####      | 4.36M/10.8M [00:00<00:00, 53.6Gb/s]
#  41%|####      | 4.39M/10.8M [00:00<00:00, 67.2Gb/s]
#  41%|####      | 4.42M/10.8M [00:00<00:00, 34.0Gb/s]
#  41%|####1     | 4.46M/10.8M [00:00<00:00, 70.0Gb/s]
#  42%|####1     | 4.49M/10.8M [00:00<00:00, 75.3Gb/s]
#  42%|####1     | 4.52M/10.8M [00:00<00:00, 16.3Gb/s]
#  42%|####2     | 4.55M/10.8M [00:00<00:00, 53.7Gb/s]
#  42%|####2     | 4.59M/10.8M [00:00<00:00, 57.4Gb/s]
#  43%|####2     | 4.62M/10.8M [00:00<00:00, 71.2Gb/s]
#  43%|####3     | 4.65M/10.8M [00:00<00:00, 61.4Gb/s]
#  43%|####3     | 4.69M/10.8M [00:00<00:00, 44.2Gb/s]
#  44%|####3     | 4.72M/10.8M [00:00<00:00, 30.6Gb/s]
#  44%|####3     | 4.75M/10.8M [00:00<00:00, 76.6Gb/s]
#  44%|####4     | 4.78M/10.8M [00:00<00:00, 81.2Gb/s]
#  45%|####4     | 4.82M/10.8M [00:00<00:00, 28.2Gb/s]
#  45%|####4     | 4.85M/10.8M [00:00<00:00, 69.0Gb/s]
#  45%|####5     | 4.88M/10.8M [00:00<00:00, 82.6Gb/s]
#  45%|####5     | 4.92M/10.8M [00:00<00:00, 32.6Gb/s]
#  46%|####5     | 4.95M/10.8M [00:00<00:00, 28.9Gb/s]
#  46%|####6     | 4.98M/10.8M [00:00<00:00, 68.0Gb/s]
#  46%|####6     | 5.01M/10.8M [00:00<00:00, 34.6Gb/s]
#  47%|####6     | 5.05M/10.8M [00:00<00:00, 28.0Gb/s]
#  47%|####6     | 5.08M/10.8M [00:00<00:00, 62.8Gb/s]
#  47%|####7     | 5.11M/10.8M [00:00<00:00, 33.3Gb/s]
#  48%|####7     | 5.14M/10.8M [00:00<00:00, 67.6Gb/s]
#  48%|####7     | 5.18M/10.8M [00:00<00:00, 59.3Gb/s]
#  48%|####8     | 5.21M/10.8M [00:00<00:00, 77.2Gb/s]
#  48%|####8     | 5.24M/10.8M [00:00<00:00, 82.7Gb/s]
#  49%|####8     | 5.28M/10.8M [00:00<00:00, 89.6Gb/s]
#  49%|####9     | 5.31M/10.8M [00:00<00:00, 45.3Gb/s]
#  49%|####9     | 5.34M/10.8M [00:00<00:00, 82.4Gb/s]
#  50%|####9     | 5.37M/10.8M [00:00<00:00, 78.5Gb/s]
#  50%|#####     | 5.41M/10.8M [00:00<00:00, 8.04Gb/s]
#  50%|#####     | 5.44M/10.8M [00:00<00:00, 73.6Gb/s]
#  51%|#####     | 5.47M/10.8M [00:00<00:00, 87.3Gb/s]
#  51%|#####     | 5.51M/10.8M [00:00<00:00, 82.5Gb/s]
#  51%|#####1    | 5.54M/10.8M [00:00<00:00, 88.7Gb/s]
#  52%|#####1    | 5.57M/10.8M [00:00<00:00, 94.2Gb/s]
#  52%|#####1    | 5.60M/10.8M [00:00<00:00, 59.5Gb/s]
#  52%|#####2    | 5.64M/10.8M [00:00<00:00, 92.0Gb/s]
#  52%|#####2    | 5.67M/10.8M [00:00<00:00, 85.8Gb/s]
#  53%|#####2    | 5.70M/10.8M [00:00<00:00, 26.8Gb/s]
#  53%|#####3    | 5.73M/10.8M [00:00<00:00, 89.7Gb/s]
#  53%|#####3    | 5.77M/10.8M [00:00<00:00, 85.5Gb/s]
#  54%|#####3    | 5.80M/10.8M [00:00<00:00, 36.9Gb/s]
#  54%|#####3    | 5.83M/10.8M [00:00<00:00, 97.9Gb/s]
#  54%|#####4    | 5.87M/10.8M [00:00<00:00, 48.4Gb/s]
#  55%|#####4    | 5.90M/10.8M [00:00<00:00, 54.5Gb/s]
#  55%|#####4    | 5.93M/10.8M [00:00<00:00, 94.6Gb/s]
#  55%|#####5    | 5.96M/10.8M [00:00<00:00, 94.7Gb/s]
#  55%|#####5    | 6.00M/10.8M [00:00<00:00, 41.3Gb/s]
#  56%|#####5    | 6.03M/10.8M [00:00<00:00, 84.0Gb/s]
#  56%|#####6    | 6.06M/10.8M [00:00<00:00, 103Gb/s]
#  56%|#####6    | 6.09M/10.8M [00:00<00:00, 52.0Gb/s]
#  57%|#####6    | 6.13M/10.8M [00:00<00:00, 75.6Gb/s]
#  57%|#####6    | 6.16M/10.8M [00:00<00:00, 61.4Gb/s]
#  57%|#####7    | 6.19M/10.8M [00:00<00:00, 79.2Gb/s]
#  58%|#####7    | 6.23M/10.8M [00:00<00:00, 98.5Gb/s]
#  58%|#####7    | 6.26M/10.8M [00:00<00:00, 108Gb/s]
#  58%|#####8    | 6.29M/10.8M [00:00<00:00, 50.6Gb/s]
#  58%|#####8    | 6.32M/10.8M [00:00<00:00, 100Gb/s]
#  59%|#####8    | 6.36M/10.8M [00:00<00:00, 108Gb/s]
#  59%|#####9    | 6.39M/10.8M [00:00<00:00, 81.5Gb/s]
#  59%|#####9    | 6.42M/10.8M [00:00<00:00, 39.4Gb/s]
#  60%|#####9    | 6.46M/10.8M [00:00<00:00, 109Gb/s]
#  60%|######    | 6.49M/10.8M [00:00<00:00, 67.7Gb/s]
#  60%|######    | 6.52M/10.8M [00:00<00:00, 107Gb/s]
#  61%|######    | 6.55M/10.8M [00:00<00:00, 117Gb/s]
#  61%|######    | 6.59M/10.8M [00:00<00:00, 54.3Gb/s]
#  61%|######1   | 6.62M/10.8M [00:00<00:00, 33.1Gb/s]
#  62%|######1   | 6.65M/10.8M [00:00<00:00, 30.8Gb/s]
#  62%|######1   | 6.68M/10.8M [00:00<00:00, 45.0Gb/s]
#  62%|######2   | 6.72M/10.8M [00:00<00:00, 43.3Gb/s]
#  62%|######2   | 6.75M/10.8M [00:00<00:00, 56.3Gb/s]
#  63%|######2   | 6.78M/10.8M [00:00<00:00, 56.2Gb/s]
#  63%|######3   | 6.82M/10.8M [00:00<00:00, 22.3Gb/s]
#  63%|######3   | 6.85M/10.8M [00:00<00:00, 50.3Gb/s]
#  64%|######3   | 6.88M/10.8M [00:00<00:00, 52.5Gb/s]
#  64%|######3   | 6.91M/10.8M [00:00<00:00, 58.7Gb/s]
#  64%|######4   | 6.95M/10.8M [00:00<00:00, 78.5Gb/s]
#  65%|######4   | 6.98M/10.8M [00:00<00:00, 85.1Gb/s]
#  65%|######4   | 7.01M/10.8M [00:00<00:00, 71.4Gb/s]
#  65%|######5   | 7.05M/10.8M [00:00<00:00, 77.8Gb/s]
#  65%|######5   | 7.08M/10.8M [00:00<00:00, 61.1Gb/s]
#  66%|######5   | 7.11M/10.8M [00:00<00:00, 60.3Gb/s]
#  66%|######6   | 7.14M/10.8M [00:00<00:00, 73.1Gb/s]
#  66%|######6   | 7.18M/10.8M [00:00<00:00, 85.3Gb/s]
#  67%|######6   | 7.21M/10.8M [00:00<00:00, 22.8Gb/s]
#  67%|######6   | 7.24M/10.8M [00:00<00:00, 86.8Gb/s]
#  67%|######7   | 7.27M/10.8M [00:00<00:00, 63.0Gb/s]
#  68%|######7   | 7.31M/10.8M [00:00<00:00, 52.6Gb/s]
#  68%|######7   | 7.34M/10.8M [00:00<00:00, 43.6Gb/s]
#  68%|######8   | 7.37M/10.8M [00:00<00:00, 10.1Gb/s]
#  68%|######8   | 7.41M/10.8M [00:00<00:00, 83.3Gb/s]
#  69%|######8   | 7.44M/10.8M [00:00<00:00, 77.4Gb/s]
#  69%|######9   | 7.47M/10.8M [00:00<00:00, 99.5Gb/s]
#  69%|######9   | 7.50M/10.8M [00:00<00:00, 68.3Gb/s]
#  70%|######9   | 7.54M/10.8M [00:00<00:00, 112Gb/s]
#  70%|#######   | 7.57M/10.8M [00:00<00:00, 72.8Gb/s]
#  70%|#######   | 7.60M/10.8M [00:00<00:00, 106Gb/s]
#  71%|#######   | 7.63M/10.8M [00:00<00:00, 119Gb/s]
#  71%|#######   | 7.67M/10.8M [00:00<00:00, 53.5Gb/s]
#  71%|#######1  | 7.70M/10.8M [00:00<00:00, 93.1Gb/s]
#  72%|#######1  | 7.73M/10.8M [00:00<00:00, 100Gb/s]
#  72%|#######1  | 7.77M/10.8M [00:00<00:00, 44.9Gb/s]
#  72%|#######2  | 7.80M/10.8M [00:00<00:00, 115Gb/s]
#  72%|#######2  | 7.83M/10.8M [00:00<00:00, 98.9Gb/s]
#  73%|#######2  | 7.86M/10.8M [00:00<00:00, 115Gb/s]
#  73%|#######3  | 7.90M/10.8M [00:00<00:00, 119Gb/s]
#  73%|#######3  | 7.93M/10.8M [00:00<00:00, 133Gb/s]
#  74%|#######3  | 7.96M/10.8M [00:00<00:00, 100Gb/s]
#  74%|#######3  | 8.00M/10.8M [00:00<00:00, 76.4Gb/s]
#  74%|#######4  | 8.03M/10.8M [00:00<00:00, 102Gb/s]
#  75%|#######4  | 8.06M/10.8M [00:00<00:00, 11.6Gb/s]
#  75%|#######4  | 8.09M/10.8M [00:00<00:00, 88.9Gb/s]
#  75%|#######5  | 8.13M/10.8M [00:00<00:00, 108Gb/s]
#  75%|#######5  | 8.16M/10.8M [00:00<00:00, 44.9Gb/s]
#  76%|#######5  | 8.19M/10.8M [00:00<00:00, 129Gb/s]
#  76%|#######6  | 8.22M/10.8M [00:00<00:00, 136Gb/s]
#  76%|#######6  | 8.26M/10.8M [00:00<00:00, 17.6Gb/s]
#  77%|#######6  | 8.29M/10.8M [00:00<00:00, 126Gb/s]
#  77%|#######6  | 8.32M/10.8M [00:00<00:00, 139Gb/s]
#  77%|#######7  | 8.36M/10.8M [00:00<00:00, 14.3Gb/s]
#  78%|#######7  | 8.39M/10.8M [00:00<00:00, 94.3Gb/s]
#  78%|#######7  | 8.42M/10.8M [00:00<00:00, 127Gb/s]
#  78%|#######8  | 8.45M/10.8M [00:00<00:00, 35.7Gb/s]
#  78%|#######8  | 8.49M/10.8M [00:00<00:00, 94.9Gb/s]
#  79%|#######8  | 8.52M/10.8M [00:00<00:00, 133Gb/s]
#  79%|#######9  | 8.55M/10.8M [00:00<00:00, 56.9Gb/s]
#  79%|#######9  | 8.59M/10.8M [00:00<00:00, 136Gb/s]
#  80%|#######9  | 8.62M/10.8M [00:00<00:00, 98.8Gb/s]
#  80%|########  | 8.65M/10.8M [00:00<00:00, 81.0Gb/s]
#  80%|########  | 8.68M/10.8M [00:00<00:00, 88.2Gb/s]
#  81%|########  | 8.72M/10.8M [00:00<00:00, 118Gb/s]
#  81%|########  | 8.75M/10.8M [00:00<00:00, 2.57Gb/s]
#  81%|########1 | 8.78M/10.8M [00:00<00:00, 94.7Gb/s]
#  82%|########1 | 8.81M/10.8M [00:00<00:00, 107Gb/s]
#  82%|########1 | 8.85M/10.8M [00:00<00:00, 109Gb/s]
#  82%|########2 | 8.88M/10.8M [00:00<00:00, 65.8Gb/s]
#  82%|########2 | 8.91M/10.8M [00:00<00:00, 149Gb/s]
#  83%|########2 | 8.95M/10.8M [00:00<00:00, 17.9Gb/s]
#  83%|########3 | 8.98M/10.8M [00:00<00:00, 145Gb/s]
#  83%|########3 | 9.01M/10.8M [00:00<00:00, 126Gb/s]
#  84%|########3 | 9.04M/10.8M [00:00<00:00, 45.5Gb/s]
#  84%|########3 | 9.08M/10.8M [00:00<00:00, 144Gb/s]
#  84%|########4 | 9.11M/10.8M [00:00<00:00, 128Gb/s]
#  85%|########4 | 9.14M/10.8M [00:00<00:00, 115Gb/s]
#  85%|########4 | 9.18M/10.8M [00:00<00:00, 123Gb/s]
#  85%|########5 | 9.21M/10.8M [00:00<00:00, 149Gb/s]
#  85%|########5 | 9.24M/10.8M [00:00<00:00, 96.7Gb/s]
#  86%|########5 | 9.27M/10.8M [00:00<00:00, 124Gb/s]
#  86%|########6 | 9.31M/10.8M [00:00<00:00, 160Gb/s]
#  86%|########6 | 9.34M/10.8M [00:00<00:00, 59.3Gb/s]
#  87%|########6 | 9.37M/10.8M [00:00<00:00, 122Gb/s]
#  87%|########6 | 9.40M/10.8M [00:00<00:00, 93.9Gb/s]
#  87%|########7 | 9.44M/10.8M [00:00<00:00, 46.2Gb/s]
#  88%|########7 | 9.47M/10.8M [00:00<00:00, 106Gb/s]
#  88%|########7 | 9.50M/10.8M [00:00<00:00, 125Gb/s]
#  88%|########8 | 9.54M/10.8M [00:00<00:00, 41.7Gb/s]
#  88%|########8 | 9.57M/10.8M [00:00<00:00, 122Gb/s]
#  89%|########8 | 9.60M/10.8M [00:00<00:00, 122Gb/s]
#  89%|########9 | 9.63M/10.8M [00:00<00:00, 113Gb/s]
#  89%|########9 | 9.67M/10.8M [00:00<00:00, 78.9Gb/s]
#  90%|########9 | 9.70M/10.8M [00:00<00:00, 111Gb/s]
#  90%|######### | 9.73M/10.8M [00:00<00:00, 39.1Gb/s]
#  90%|######### | 9.76M/10.8M [00:00<00:00, 121Gb/s]
#  91%|######### | 9.80M/10.8M [00:00<00:00, 130Gb/s]
#  91%|######### | 9.83M/10.8M [00:00<00:00, 85.5Gb/s]
#  91%|#########1| 9.86M/10.8M [00:00<00:00, 121Gb/s]
#  92%|#########1| 9.90M/10.8M [00:00<00:00, 134Gb/s]
#  92%|#########1| 9.93M/10.8M [00:00<00:00, 81.0Gb/s]
#  92%|#########2| 9.96M/10.8M [00:00<00:00, 91.8Gb/s]
#  92%|#########2| 9.99M/10.8M [00:00<00:00, 92.5Gb/s]
#  93%|#########2| 10.0M/10.8M [00:00<00:00, 32.8Gb/s]
#  93%|#########3| 10.1M/10.8M [00:00<00:00, 127Gb/s]
#  93%|#########3| 10.1M/10.8M [00:00<00:00, 142Gb/s]
#  94%|#########3| 10.1M/10.8M [00:00<00:00, 78.8Gb/s]
#  94%|#########3| 10.2M/10.8M [00:00<00:00, 128Gb/s]
#  94%|#########4| 10.2M/10.8M [00:00<00:00, 131Gb/s]
#  95%|#########4| 10.2M/10.8M [00:00<00:00, 117Gb/s]
#  95%|#########4| 10.3M/10.8M [00:00<00:00, 132Gb/s]
#  95%|#########5| 10.3M/10.8M [00:00<00:00, 135Gb/s]
#  95%|#########5| 10.3M/10.8M [00:00<00:00, 46.9Gb/s]
#  96%|#########5| 10.4M/10.8M [00:00<00:00, 135Gb/s]
#  96%|#########6| 10.4M/10.8M [00:00<00:00, 141Gb/s]
#  96%|#########6| 10.4M/10.8M [00:00<00:00, 33.9Gb/s]
#  97%|#########6| 10.5M/10.8M [00:00<00:00, 137Gb/s]
#  97%|#########6| 10.5M/10.8M [00:00<00:00, 141Gb/s]
#  97%|#########7| 10.5M/10.8M [00:00<00:00, 118Gb/s]
#  98%|#########7| 10.6M/10.8M [00:00<00:00, 135Gb/s]
#  98%|#########7| 10.6M/10.8M [00:00<00:00, 140Gb/s]
#  98%|#########8| 10.6M/10.8M [00:00<00:00, 47.7Gb/s]
#  99%|#########8| 10.6M/10.8M [00:00<00:00, 131Gb/s]
#  99%|#########8| 10.7M/10.8M [00:00<00:00, 146Gb/s]
#  99%|#########9| 10.7M/10.8M [00:00<00:00, 48.8Gb/s]
#  99%|#########9| 10.7M/10.8M [00:00<00:00, 144Gb/s]
# 100%|#########9| 10.8M/10.8M [00:00<00:00, 147Gb/s]
# 100%|##########| 10.8M/10.8M [00:00<00:00, 156Gb/s]
#
# Process finished with exit code 0



#Invoking viewBar

# A is  32768
# B is  10811677
# Complete Percent : 0.30 %A is  65536
# B is  10811677
# Complete Percent : 0.61 %A is  98304
# B is  10811677
# Complete Percent : 0.91 %A is  131072
# B is  10811677
# Complete Percent : 1.21 %A is  163840
# B is  10811677
# Complete Percent : 1.52 %A is  196608
# B is  10811677
# Complete Percent : 1.82 %A is  229376
# B is  10811677
# Complete Percent : 2.12 %A is  262144
# B is  10811677
# Complete Percent : 2.42 %A is  294912
# B is  10811677
# Complete Percent : 2.73 %A is  327680
# B is  10811677
# Complete Percent : 3.03 %A is  360448
# B is  10811677
# Complete Percent : 3.33 %A is  393216
# B is  10811677
# Complete Percent : 3.64 %A is  425984
# B is  10811677
# Complete Percent : 3.94 %A is  458752
# B is  10811677
# Complete Percent : 4.24 %A is  491520
# B is  10811677
# Complete Percent : 4.55 %A is  524288
# B is  10811677
# Complete Percent : 4.85 %A is  557056
# B is  10811677
# Complete Percent : 5.15 %A is  589824
# B is  10811677
# Complete Percent : 5.46 %A is  622592
# B is  10811677
# Complete Percent : 5.76 %A is  655360
# B is  10811677
# Complete Percent : 6.06 %A is  688128
# B is  10811677
# Complete Percent : 6.36 %A is  720896
# B is  10811677
# Complete Percent : 6.67 %A is  753664
# B is  10811677
# Complete Percent : 6.97 %A is  786432
# B is  10811677
# Complete Percent : 7.27 %A is  819200
# B is  10811677
# Complete Percent : 7.58 %A is  851968
# B is  10811677
# Complete Percent : 7.88 %A is  884736
# B is  10811677
# Complete Percent : 8.18 %A is  917504
# B is  10811677
# Complete Percent : 8.49 %A is  950272
# B is  10811677
# Complete Percent : 8.79 %A is  983040
# B is  10811677
# Complete Percent : 9.09 %A is  1015808
# B is  10811677
# Complete Percent : 9.40 %A is  1048576
# B is  10811677
# Complete Percent : 9.70 %A is  1081344
# B is  10811677
# Complete Percent : 10.00 %A is  1114112
# B is  10811677
# Complete Percent : 10.30 %A is  1146880
# B is  10811677
# Complete Percent : 10.61 %A is  1179648
# B is  10811677
# Complete Percent : 10.91 %A is  1212416
# B is  10811677
# Complete Percent : 11.21 %A is  1245184
# B is  10811677
# Complete Percent : 11.52 %A is  1277952
# B is  10811677
# Complete Percent : 11.82 %A is  1310720
# B is  10811677
# Complete Percent : 12.12 %A is  1343488
# B is  10811677
# Complete Percent : 12.43 %A is  1376256
# B is  10811677
# Complete Percent : 12.73 %A is  1409024
# B is  10811677
# Complete Percent : 13.03 %A is  1441792
# B is  10811677
# Complete Percent : 13.34 %A is  1474560
# B is  10811677
# Complete Percent : 13.64 %A is  1507328
# B is  10811677
# Complete Percent : 13.94 %A is  1540096
# B is  10811677
# Complete Percent : 14.24 %A is  1572864
# B is  10811677
# Complete Percent : 14.55 %A is  1605632
# B is  10811677
# Complete Percent : 14.85 %A is  1638400
# B is  10811677
# Complete Percent : 15.15 %A is  1671168
# B is  10811677
# Complete Percent : 15.46 %A is  1703936
# B is  10811677
# Complete Percent : 15.76 %A is  1736704
# B is  10811677
# Complete Percent : 16.06 %A is  1769472
# B is  10811677
# Complete Percent : 16.37 %A is  1802240
# B is  10811677
# Complete Percent : 16.67 %A is  1835008
# B is  10811677
# Complete Percent : 16.97 %A is  1867776
# B is  10811677
# Complete Percent : 17.28 %A is  1900544
# B is  10811677
# Complete Percent : 17.58 %A is  1933312
# B is  10811677
# Complete Percent : 17.88 %A is  1966080
# B is  10811677
# Complete Percent : 18.18 %A is  1998848
# B is  10811677
# Complete Percent : 18.49 %A is  2031616
# B is  10811677
# Complete Percent : 18.79 %A is  2064384
# B is  10811677
# Complete Percent : 19.09 %A is  2097152
# B is  10811677
# Complete Percent : 19.40 %A is  2129920
# B is  10811677
# Complete Percent : 19.70 %A is  2162688
# B is  10811677
# Complete Percent : 20.00 %A is  2195456
# B is  10811677
# Complete Percent : 20.31 %A is  2228224
# B is  10811677
# Complete Percent : 20.61 %A is  2260992
# B is  10811677
# Complete Percent : 20.91 %A is  2293760
# B is  10811677
# Complete Percent : 21.22 %A is  2326528
# B is  10811677
# Complete Percent : 21.52 %A is  2359296
# B is  10811677
# Complete Percent : 21.82 %A is  2392064
# B is  10811677
# Complete Percent : 22.12 %A is  2424832
# B is  10811677
# Complete Percent : 22.43 %A is  2457600
# B is  10811677
# Complete Percent : 22.73 %A is  2490368
# B is  10811677
# Complete Percent : 23.03 %A is  2523136
# B is  10811677
# Complete Percent : 23.34 %A is  2555904
# B is  10811677
# Complete Percent : 23.64 %A is  2588672
# B is  10811677
# Complete Percent : 23.94 %A is  2621440
# B is  10811677
# Complete Percent : 24.25 %A is  2654208
# B is  10811677
# Complete Percent : 24.55 %A is  2686976
# B is  10811677
# Complete Percent : 24.85 %A is  2719744
# B is  10811677
# Complete Percent : 25.16 %A is  2752512
# B is  10811677
# Complete Percent : 25.46 %A is  2785280
# B is  10811677
# Complete Percent : 25.76 %A is  2818048
# B is  10811677
# Complete Percent : 26.06 %A is  2850816
# B is  10811677
# Complete Percent : 26.37 %A is  2883584
# B is  10811677
# Complete Percent : 26.67 %A is  2916352
# B is  10811677
# Complete Percent : 26.97 %A is  2949120
# B is  10811677
# Complete Percent : 27.28 %A is  2981888
# B is  10811677
# Complete Percent : 27.58 %A is  3014656
# B is  10811677
# Complete Percent : 27.88 %A is  3047424
# B is  10811677
# Complete Percent : 28.19 %A is  3080192
# B is  10811677
# Complete Percent : 28.49 %A is  3112960
# B is  10811677
# Complete Percent : 28.79 %A is  3145728
# B is  10811677
# Complete Percent : 29.10 %A is  3178496
# B is  10811677
# Complete Percent : 29.40 %A is  3211264
# B is  10811677
# Complete Percent : 29.70 %A is  3244032
# B is  10811677
# Complete Percent : 30.00 %A is  3276800
# B is  10811677
# Complete Percent : 30.31 %A is  3309568
# B is  10811677
# Complete Percent : 30.61 %A is  3342336
# B is  10811677
# Complete Percent : 30.91 %A is  3375104
# B is  10811677
# Complete Percent : 31.22 %A is  3407872
# B is  10811677
# Complete Percent : 31.52 %A is  3440640
# B is  10811677
# Complete Percent : 31.82 %A is  3473408
# B is  10811677
# Complete Percent : 32.13 %A is  3506176
# B is  10811677
# Complete Percent : 32.43 %A is  3538944
# B is  10811677
# Complete Percent : 32.73 %A is  3571712
# B is  10811677
# Complete Percent : 33.04 %A is  3604480
# B is  10811677
# Complete Percent : 33.34 %A is  3637248
# B is  10811677
# Complete Percent : 33.64 %A is  3670016
# B is  10811677
# Complete Percent : 33.94 %A is  3702784
# B is  10811677
# Complete Percent : 34.25 %A is  3735552
# B is  10811677
# Complete Percent : 34.55 %A is  3768320
# B is  10811677
# Complete Percent : 34.85 %A is  3801088
# B is  10811677
# Complete Percent : 35.16 %A is  3833856
# B is  10811677
# Complete Percent : 35.46 %A is  3866624
# B is  10811677
# Complete Percent : 35.76 %A is  3899392
# B is  10811677
# Complete Percent : 36.07 %A is  3932160
# B is  10811677
# Complete Percent : 36.37 %A is  3964928
# B is  10811677
# Complete Percent : 36.67 %A is  3997696
# B is  10811677
# Complete Percent : 36.98 %A is  4030464
# B is  10811677
# Complete Percent : 37.28 %A is  4063232
# B is  10811677
# Complete Percent : 37.58 %A is  4096000
# B is  10811677
# Complete Percent : 37.88 %A is  4128768
# B is  10811677
# Complete Percent : 38.19 %A is  4161536
# B is  10811677
# Complete Percent : 38.49 %A is  4194304
# B is  10811677
# Complete Percent : 38.79 %A is  4227072
# B is  10811677
# Complete Percent : 39.10 %A is  4259840
# B is  10811677
# Complete Percent : 39.40 %A is  4292608
# B is  10811677
# Complete Percent : 39.70 %A is  4325376
# B is  10811677
# Complete Percent : 40.01 %A is  4358144
# B is  10811677
# Complete Percent : 40.31 %A is  4390912
# B is  10811677
# Complete Percent : 40.61 %A is  4423680
# B is  10811677
# Complete Percent : 40.92 %A is  4456448
# B is  10811677
# Complete Percent : 41.22 %A is  4489216
# B is  10811677
# Complete Percent : 41.52 %A is  4521984
# B is  10811677
# Complete Percent : 41.83 %A is  4554752
# B is  10811677
# Complete Percent : 42.13 %A is  4587520
# B is  10811677
# Complete Percent : 42.43 %A is  4620288
# B is  10811677
# Complete Percent : 42.73 %A is  4653056
# B is  10811677
# Complete Percent : 43.04 %A is  4685824
# B is  10811677
# Complete Percent : 43.34 %A is  4718592
# B is  10811677
# Complete Percent : 43.64 %A is  4751360
# B is  10811677
# Complete Percent : 43.95 %A is  4784128
# B is  10811677
# Complete Percent : 44.25 %A is  4816896
# B is  10811677
# Complete Percent : 44.55 %A is  4849664
# B is  10811677
# Complete Percent : 44.86 %A is  4882432
# B is  10811677
# Complete Percent : 45.16 %A is  4915200
# B is  10811677
# Complete Percent : 45.46 %A is  4947968
# B is  10811677
# Complete Percent : 45.77 %A is  4980736
# B is  10811677
# Complete Percent : 46.07 %A is  5013504
# B is  10811677
# Complete Percent : 46.37 %A is  5046272
# B is  10811677
# Complete Percent : 46.67 %A is  5079040
# B is  10811677
# Complete Percent : 46.98 %A is  5111808
# B is  10811677
# Complete Percent : 47.28 %A is  5144576
# B is  10811677
# Complete Percent : 47.58 %A is  5177344
# B is  10811677
# Complete Percent : 47.89 %A is  5210112
# B is  10811677
# Complete Percent : 48.19 %A is  5242880
# B is  10811677
# Complete Percent : 48.49 %A is  5275648
# B is  10811677
# Complete Percent : 48.80 %A is  5308416
# B is  10811677
# Complete Percent : 49.10 %A is  5341184
# B is  10811677
# Complete Percent : 49.40 %A is  5373952
# B is  10811677
# Complete Percent : 49.71 %A is  5406720
# B is  10811677
# Complete Percent : 50.01 %A is  5439488
# B is  10811677
# Complete Percent : 50.31 %A is  5472256
# B is  10811677
# Complete Percent : 50.61 %A is  5505024
# B is  10811677
# Complete Percent : 50.92 %A is  5537792
# B is  10811677
# Complete Percent : 51.22 %A is  5570560
# B is  10811677
# Complete Percent : 51.52 %A is  5603328
# B is  10811677
# Complete Percent : 51.83 %A is  5636096
# B is  10811677
# Complete Percent : 52.13 %A is  5668864
# B is  10811677
# Complete Percent : 52.43 %A is  5701632
# B is  10811677
# Complete Percent : 52.74 %A is  5734400
# B is  10811677
# Complete Percent : 53.04 %A is  5767168
# B is  10811677
# Complete Percent : 53.34 %A is  5799936
# B is  10811677
# Complete Percent : 53.65 %A is  5832704
# B is  10811677
# Complete Percent : 53.95 %A is  5865472
# B is  10811677
# Complete Percent : 54.25 %A is  5898240
# B is  10811677
# Complete Percent : 54.55 %A is  5931008
# B is  10811677
# Complete Percent : 54.86 %A is  5963776
# B is  10811677
# Complete Percent : 55.16 %A is  5996544
# B is  10811677
# Complete Percent : 55.46 %A is  6029312
# B is  10811677
# Complete Percent : 55.77 %A is  6062080
# B is  10811677
# Complete Percent : 56.07 %A is  6094848
# B is  10811677
# Complete Percent : 56.37 %A is  6127616
# B is  10811677
# Complete Percent : 56.68 %A is  6160384
# B is  10811677
# Complete Percent : 56.98 %A is  6193152
# B is  10811677
# Complete Percent : 57.28 %A is  6225920
# B is  10811677
# Complete Percent : 57.59 %A is  6258688
# B is  10811677
# Complete Percent : 57.89 %A is  6291456
# B is  10811677
# Complete Percent : 58.19 %A is  6324224
# B is  10811677
# Complete Percent : 58.49 %A is  6356992
# B is  10811677
# Complete Percent : 58.80 %A is  6389760
# B is  10811677
# Complete Percent : 59.10 %A is  6422528
# B is  10811677
# Complete Percent : 59.40 %A is  6455296
# B is  10811677
# Complete Percent : 59.71 %A is  6488064
# B is  10811677
# Complete Percent : 60.01 %A is  6520832
# B is  10811677
# Complete Percent : 60.31 %A is  6553600
# B is  10811677
# Complete Percent : 60.62 %A is  6586368
# B is  10811677
# Complete Percent : 60.92 %A is  6619136
# B is  10811677
# Complete Percent : 61.22 %A is  6651904
# B is  10811677
# Complete Percent : 61.53 %A is  6684672
# B is  10811677
# Complete Percent : 61.83 %A is  6717440
# B is  10811677
# Complete Percent : 62.13 %A is  6750208
# B is  10811677
# Complete Percent : 62.43 %A is  6782976
# B is  10811677
# Complete Percent : 62.74 %A is  6815744
# B is  10811677
# Complete Percent : 63.04 %A is  6848512
# B is  10811677
# Complete Percent : 63.34 %A is  6881280
# B is  10811677
# Complete Percent : 63.65 %A is  6914048
# B is  10811677
# Complete Percent : 63.95 %A is  6946816
# B is  10811677
# Complete Percent : 64.25 %A is  6979584
# B is  10811677
# Complete Percent : 64.56 %A is  7012352
# B is  10811677
# Complete Percent : 64.86 %A is  7045120
# B is  10811677
# Complete Percent : 65.16 %A is  7077888
# B is  10811677
# Complete Percent : 65.47 %A is  7110656
# B is  10811677
# Complete Percent : 65.77 %A is  7143424
# B is  10811677
# Complete Percent : 66.07 %A is  7176192
# B is  10811677
# Complete Percent : 66.37 %A is  7208960
# B is  10811677
# Complete Percent : 66.68 %A is  7241728
# B is  10811677
# Complete Percent : 66.98 %A is  7274496
# B is  10811677
# Complete Percent : 67.28 %A is  7307264
# B is  10811677
# Complete Percent : 67.59 %A is  7340032
# B is  10811677
# Complete Percent : 67.89 %A is  7372800
# B is  10811677
# Complete Percent : 68.19 %A is  7405568
# B is  10811677
# Complete Percent : 68.50 %A is  7438336
# B is  10811677
# Complete Percent : 68.80 %A is  7471104
# B is  10811677
# Complete Percent : 69.10 %A is  7503872
# B is  10811677
# Complete Percent : 69.41 %A is  7536640
# B is  10811677
# Complete Percent : 69.71 %A is  7569408
# B is  10811677
# Complete Percent : 70.01 %A is  7602176
# B is  10811677
# Complete Percent : 70.31 %A is  7634944
# B is  10811677
# Complete Percent : 70.62 %A is  7667712
# B is  10811677
# Complete Percent : 70.92 %A is  7700480
# B is  10811677
# Complete Percent : 71.22 %A is  7733248
# B is  10811677
# Complete Percent : 71.53 %A is  7766016
# B is  10811677
# Complete Percent : 71.83 %A is  7798784
# B is  10811677
# Complete Percent : 72.13 %A is  7831552
# B is  10811677
# Complete Percent : 72.44 %A is  7864320
# B is  10811677
# Complete Percent : 72.74 %A is  7897088
# B is  10811677
# Complete Percent : 73.04 %A is  7929856
# B is  10811677
# Complete Percent : 73.35 %A is  7962624
# B is  10811677
# Complete Percent : 73.65 %A is  7995392
# B is  10811677
# Complete Percent : 73.95 %A is  8028160
# B is  10811677
# Complete Percent : 74.25 %A is  8060928
# B is  10811677
# Complete Percent : 74.56 %A is  8093696
# B is  10811677
# Complete Percent : 74.86 %A is  8126464
# B is  10811677
# Complete Percent : 75.16 %A is  8159232
# B is  10811677
# Complete Percent : 75.47 %A is  8192000
# B is  10811677
# Complete Percent : 75.77 %A is  8224768
# B is  10811677
# Complete Percent : 76.07 %A is  8257536
# B is  10811677
# Complete Percent : 76.38 %A is  8290304
# B is  10811677
# Complete Percent : 76.68 %A is  8323072
# B is  10811677
# Complete Percent : 76.98 %A is  8355840
# B is  10811677
# Complete Percent : 77.29 %A is  8388608
# B is  10811677
# Complete Percent : 77.59 %A is  8421376
# B is  10811677
# Complete Percent : 77.89 %A is  8454144
# B is  10811677
# Complete Percent : 78.19 %A is  8486912
# B is  10811677
# Complete Percent : 78.50 %A is  8519680
# B is  10811677
# Complete Percent : 78.80 %A is  8552448
# B is  10811677
# Complete Percent : 79.10 %A is  8585216
# B is  10811677
# Complete Percent : 79.41 %A is  8617984
# B is  10811677
# Complete Percent : 79.71 %A is  8650752
# B is  10811677
# Complete Percent : 80.01 %A is  8683520
# B is  10811677
# Complete Percent : 80.32 %A is  8716288
# B is  10811677
# Complete Percent : 80.62 %A is  8749056
# B is  10811677
# Complete Percent : 80.92 %A is  8781824
# B is  10811677
# Complete Percent : 81.23 %A is  8814592
# B is  10811677
# Complete Percent : 81.53 %A is  8847360
# B is  10811677
# Complete Percent : 81.83 %A is  8880128
# B is  10811677
# Complete Percent : 82.13 %A is  8912896
# B is  10811677
# Complete Percent : 82.44 %A is  8945664
# B is  10811677
# Complete Percent : 82.74 %A is  8978432
# B is  10811677
# Complete Percent : 83.04 %A is  9011200
# B is  10811677
# Complete Percent : 83.35 %A is  9043968
# B is  10811677
# Complete Percent : 83.65 %A is  9076736
# B is  10811677
# Complete Percent : 83.95 %A is  9109504
# B is  10811677
# Complete Percent : 84.26 %A is  9142272
# B is  10811677
# Complete Percent : 84.56 %A is  9175040
# B is  10811677
# Complete Percent : 84.86 %A is  9207808
# B is  10811677
# Complete Percent : 85.17 %A is  9240576
# B is  10811677
# Complete Percent : 85.47 %A is  9273344
# B is  10811677
# Complete Percent : 85.77 %A is  9306112
# B is  10811677
# Complete Percent : 86.07 %A is  9338880
# B is  10811677
# Complete Percent : 86.38 %A is  9371648
# B is  10811677
# Complete Percent : 86.68 %A is  9404416
# B is  10811677
# Complete Percent : 86.98 %A is  9437184
# B is  10811677
# Complete Percent : 87.29 %A is  9469952
# B is  10811677
# Complete Percent : 87.59 %A is  9502720
# B is  10811677
# Complete Percent : 87.89 %A is  9535488
# B is  10811677
# Complete Percent : 88.20 %A is  9568256
# B is  10811677
# Complete Percent : 88.50 %A is  9601024
# B is  10811677
# Complete Percent : 88.80 %A is  9633792
# B is  10811677
# Complete Percent : 89.11 %A is  9666560
# B is  10811677
# Complete Percent : 89.41 %A is  9699328
# B is  10811677
# Complete Percent : 89.71 %A is  9732096
# B is  10811677
# Complete Percent : 90.01 %A is  9764864
# B is  10811677
# Complete Percent : 90.32 %A is  9797632
# B is  10811677
# Complete Percent : 90.62 %A is  9830400
# B is  10811677
# Complete Percent : 90.92 %A is  9863168
# B is  10811677
# Complete Percent : 91.23 %A is  9895936
# B is  10811677
# Complete Percent : 91.53 %A is  9928704
# B is  10811677
# Complete Percent : 91.83 %A is  9961472
# B is  10811677
# Complete Percent : 92.14 %A is  9994240
# B is  10811677
# Complete Percent : 92.44 %A is  10027008
# B is  10811677
# Complete Percent : 92.74 %A is  10059776
# B is  10811677
# Complete Percent : 93.05 %A is  10092544
# B is  10811677
# Complete Percent : 93.35 %A is  10125312
# B is  10811677
# Complete Percent : 93.65 %A is  10158080
# B is  10811677
# Complete Percent : 93.95 %A is  10190848
# B is  10811677
# Complete Percent : 94.26 %A is  10223616
# B is  10811677
# Complete Percent : 94.56 %A is  10256384
# B is  10811677
# Complete Percent : 94.86 %A is  10289152
# B is  10811677
# Complete Percent : 95.17 %A is  10321920
# B is  10811677
# Complete Percent : 95.47 %A is  10354688
# B is  10811677
# Complete Percent : 95.77 %A is  10387456
# B is  10811677
# Complete Percent : 96.08 %A is  10420224
# B is  10811677
# Complete Percent : 96.38 %A is  10452992
# B is  10811677
# Complete Percent : 96.68 %A is  10485760
# B is  10811677
# Complete Percent : 96.99 %A is  10518528
# B is  10811677
# Complete Percent : 97.29 %A is  10551296
# B is  10811677
# Complete Percent : 97.59 %A is  10584064
# B is  10811677
# Complete Percent : 97.89 %A is  10616832
# B is  10811677
# Complete Percent : 98.20 %A is  10649600
# B is  10811677
# Complete Percent : 98.50 %A is  10682368
# B is  10811677
# Complete Percent : 98.80 %A is  10715136
# B is  10811677
# Complete Percent : 99.11 %A is  10747904
# B is  10811677
# Complete Percent : 99.41 %A is  10780672
# B is  10811677
# Complete Percent : 99.71 %A is  10811677
# B is  10811677
# Complete Percent : 100.00 %
