from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

def applyModel_classification(estimator,x_train,y_train,x_test,y_test):
    model = estimator
    model.fit(x_train,y_train)
    # get the classification report
    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)
    # check the accuracy
    print("Train Score: ", model.score(x_train,y_train))
    print("Test Score: ", model.score(x_test,y_test))
    print("")
    print("################## Classification Report : Train ##########################")
    print(classification_report(y_train,y_train_pred))
    print("_______________________________________________________________________________")

    print("################## Classification Report : Test ##########################")
    print(classification_report(y_test,y_test_pred))
    print("_______________________________________________________________________________")
    return(model)