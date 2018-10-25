
#testing whether tar is exist or not
import tarfile

for filename in ['answer_correction.py',
                 'model.csv']:
    try:
        print('{:>15}  {}'.format(filename, tarfile.is_tarfile(
            filename)))
    except IOError as err:
        print('{:>15}  {}'.format(filename, err))

