from setuptools import setup, find_packages

setup(
    name='ferum_customs',
    version='1.0.0',
    description='Ferum Customizations for ERPNext',
    author='Your Name',
    author_email='you@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)
