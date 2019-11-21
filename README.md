## Materials Project Lectures

Assets for the Materials Project lectures taught in the Fall 2019 semester of MSE 215.


1. Go to: 
github.com/mse215/mplectures

2. Click “Clone or Download” (green) 

3. Copy the url that appears. 
`>> git clone <paste_url> `

4. Create Conda Env
`>> conda create -n mse215 python=3`

5. Activate Env
`>> conda activate mse215`
(Error? try `source activate mse215`) 

6. Enter mplectures directory
`>> cd mplectures`

7. Install dependencies
`>> pip install -r requirements.txt`

Done!

## Tests

The following will check that all notebooks run properly.

```python
python setup.py install
pip install -r requirements.txt
python test.py
```

If you get an error like
> `jupyter_client.kernelspec.NoSuchKernel: No such kernel named <ENVNAME>`

then that notebook expects to be run using an IPython kernel with that name. With your Python environment activated, run
```
python -m ipykernel install --user --name <ENVNAME>
```
where `<ENVNAME>` is the name in the error message, e.g. `conda-env-mp-py`. This will ensure that the notebook uses your local environment. to run itself.

