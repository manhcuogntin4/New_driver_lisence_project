import numpy as np
import scipy
from scipy.stats import norm

import sys,os

import math
def normpdf(x, mean, sd):
    var = float(sd)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    #print ss
    return ss

def pstdev(data):
    """Calculates the population standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    print ss
    pvar = 1.0*ss/n # the population variance
    print n, pvar
    return pvar**0.5

caffe_root = '/home/cuong-nguyen/2016/Workspace/brexia/Septembre/Codesource/caffe-master'

sys.path.insert(0, caffe_root + 'python')

import caffe

os.chdir(caffe_root)

 

net_file='/home/cuong-nguyen/2017/Workspace/Fevrier/CodeSource/AnnotationTool/AnnotationTool/python/document_category_googlenet/deploy.prototxt'

caffe_model='/home/cuong-nguyen/2017/Workspace/Fevrier/CodeSource/AnnotationTool/AnnotationTool/python/document_category_googlenet/train_val.caffemodel'

mean_file='/home/cuong-nguyen/2016/Workspace/brexia/Decembre/CodeSource/codeHaoming/web-demo-version4.0/caffe-fast-rcnn/python/caffe/imagenet'

 

net = caffe.Net(net_file,caffe_model,caffe.TEST)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

transformer.set_transpose('data', (2,0,1))

#transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))

transformer.set_raw_scale('data', 255)

transformer.set_channel_swap('data', (2,1,0)) # if using RGB instead if BGR

 

#im=caffe.io.load_image(caffe_root+'examples/images/cat.jpg')

img=caffe.io.load_image('/home/cuong-nguyen/2017/Workspace/Fevrier/CodeSource/AnnotationTool/AnnotationTool/python/document_category_googlenet/t.png')

#img=caffe.io.load_image('/home/cuong-nguyen/2017/Workspace/Fevrier/Documents/prefix-1.png')

net.blobs['data'].data[...] = transformer.preprocess('data',img)

out = net.forward()
print out 

proba = out['prob'][0]
scores = net.blobs['fc8'].data[0]
print proba, scores
#top_k= out['fc8'][0]

imagenet_labels_filename ='/home/cuong-nguyen/2017/Workspace/Fevrier/CodeSource/AnnotationTool/AnnotationTool/python/document_category_googlenet/synset_words.txt'

labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

print labels 

#top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
# top_k = net.blobs['fc8'].data[0].flatten().argsort()[-1:-6:-1]

# print top_k
# top_k= out['fc8'][0]
# m=mean(top_k)
# p=pstdev(top_k)
# #print normpdf(top_k[2], m, p)
# out=(top_k-m)/p
# pro=1-norm.cdf(out)
# #print pro
# pro1=scipy.stats.norm(m, p).cdf(top_k)
# print pro1
# #print out, pro, pro1
#print pro1
#indices = (-proba).argsort()[:3]
#print indices
#print top_k, m, p


# for i in np.arange(top_k.size):

#     print top_k[i], labels[top_k[i]]