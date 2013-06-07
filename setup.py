import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-feedback-form',
    version='0.1',
    packages=['feedback_form'],
    include_package_data=True,
    license='BSD License',
    description='Put short description here...',
    long_description=README,
    url='http://github.com/bashu/django-feedback-form',
    author='Basil Shubin',
    install_requires=[
        'django-contact-form-dev',
        'django-crispy-forms',
    ],
    dependency_links = [
        'http://github.com/bashu/django-contact-form/tarball/master#egg=django-contact-form-dev',
    ],
    author_email='basil.shubin@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
