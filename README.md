The quality assurance of cacao beans that
involves classification of fermented or defected cacao beans
are done through visual inspections by agricultural
technicians, which can result to errors and consistencies.
This study developed a computer-based classifier of
fermented or defected cacao beans with an added feature of
bean count using load cell. The researchers test the accuracy
of SVM classifier with five trials and bean count with ten
trials. The captured image initially goes through pre-
processing followed by feature extraction, then the features
extracted undergoes K-means clustering and standard
scaling. The image is classified whether it is fermented,
mouldy, slaty or germinated cacao bean. The SVM classifier
was tested in different watts of bulb, number of bulb used,
different values for K-means clustering and iteration. The
SVM classifier shows an average success rate of 92% and an
average kappa index agreement of 0.89. 


# SVM_classifier
Place images to train in a separate folder based on their classes. 
sample train command:
$ python train.py –t dataset/train
sample test command:
$ python classify.py –t dataset/test/ -v
