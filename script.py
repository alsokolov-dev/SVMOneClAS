import sys

def main(trainDataFile, testDataFile):
    #Open files, read the data and create "numpy" arrays
    train, test = createNumpyArrays(trainDataFile, testDataFile)

    #Performing scale normalization
    train_scale, test_scale = scaleNormalization(train, test)

    #Filter out genes with negative values (possible non expressed genes)
    train_filter=[]
    for row in train_scale:
        if row[0]>0 and row[1]>0:
            train_filter.append(row[:])
    train_filter = np.array(train_filter)

    #Creating data for cross validation analysis (test size = 40% by default)
    X_train, X_test = cross_validation.train_test_split(train_filter, test_size=0.3, random_state=0)

    #Fiting the best parameters
    error_train = fitingBestParameters(X_train, X_test)

    #Choosing best parameters
    best_kernel = chooseBestParameter(error_train)

    #Fiting classifier with best parameters
    clf = svm.OneClassSVM(kernel = best_kernel, nu=0.01)
    clf.fit(train_filter)

    #Predicting new events of alternative splicing
    prd = clf.predict(test_scale)

    #Output results
    output = prd[prd == 1].size/float(prd.size)*100
    print ("Predicted new events of alternative splicing / all events of alternative splicing ratio: " + str(output) + "%")
    file = open("results.txt", 'w')
    for line in prd:
        file.write(str(line)+"\n")
    file.close()

def createNumpyArrays(trainDataFile, testDataFile):
    #Set up containers for train and test data
    train = []
    test = []

    #Open files and read the data
    file = open("ref_final.txt",'r')
    for row in file:
        train.append(row.strip().split('\t')[1:])
    file = open("alt_final.txt",'r')
    for row in file:
        test.append(row.strip().split('\t')[1:])

    #Creating "numpy" arrays
    train = np.array(train, dtype=float)
    test = np.array(test, dtype=float)

    return train, test

def scaleNormalization(train, test):
    #Performing scale normalization (for each value subtract mean and then divide by SD)
    test_scale = preprocessing.scale(test)
    train_scale = preprocessing.scale(train)

    return train_scale, test_scale

def fitingBestParameters(X_train, X_test):
    #Fiting the best parameters
    error_train = {} 
    for kernel_type in ["linear", "poly", "rbf","sigmoid"]:
        if kernel_type!="linear":
            for deg in [1,2,3,4,5]:
                for g in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]:
                    clf = svm.OneClassSVM(kernel=kernel_type,nu=0.01)
                    clf.fit(X_train)
                    prd = clf.predict(X_test)
                    error = prd[prd == -1].size/float(prd.size)*100
                    error_train[kernel_type+"-degree="+str(deg)+"-gamma="+str(g)]=error 
                    print(kernel_type+" degree = "+str(deg)+" gamma = "+str(g)+"    "+str(error))
        else:
            clf = svm.OneClassSVM(kernel=kernel_type,nu=0.01)
            clf.fit(X_train)
            prd = clf.predict(X_test)
            error = prd[prd == -1].size/float(prd.size)*100
            error_train[kernel_type]=error
            print(kernel_type+" "+str(error))

    return error_train

def chooseBestParameter(error_train):
    #Choosing best parameters
    best_kernel=''
    best_value=100
    for name in error_train:
        if error_train[name]<best_value:
            best_kernel=name
            best_value=error_train[name]
    print ("The best kernel is '"+best_kernel+"' with cross validation error - "+str(best_value))

    return best_kernel

if __name__ == "__main__":
    # check whether numpy is installed
    try:
        import numpy as np
    except ImportError:
        sys.exit("numpy is not installed")

    # check whether sklearn is installed
    try:
        from sklearn import preprocessing, cross_validation, svm
    except ImportError:
        sys.exit("scikit-learn library is not installed")

    # check whether user provided script with input files
    try:
        trainDataFile = sys.argv[1]
    except IndexError:
        sys.exit("Please provide file for train data")

    try:
        testDataFile = sys.argv[2]
    except IndexError:
        sys.exit("Please provide file for test data")

    # Inflate main function
    main(trainDataFile, testDataFile)