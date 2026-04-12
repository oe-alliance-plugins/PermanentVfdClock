from setuptools import setup
import setup_translate

pkg = 'Extensions.PermanentVfdClock'
setup(name='enigma2-plugin-extensions-permanentvfdclock',
       version='1.0',
       description='Show clock in VFD permanently',
       package_dir={pkg: 'PermanentVfdClock'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
