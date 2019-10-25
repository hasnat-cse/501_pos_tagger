Team Members:
    Arnob Mallik (CCID: amallik)
    Arif Hasnat (CCID: hasnat)


INSTALL:

pip3 install dill

Execution Instructions:
    To test using stanford pos tagger, run following command from command line:
        python3 pos_stanford_test.py --jar PATH_TO_STANFORD_TAGGER_JAR --model PATH_TO_MODEL_FILE --test PATH_TO_TEST_FILE

        example: python3 pos_stanford_train.py --jar StanfordTagger/stanford-postagger.jar --model StanfordTagger/Stanford1
                    --test A3DataCleaned/Domain1Test.txt


    To train using stanford pos tagger, run following command from command line:
        python3 pos_stanford_train.py --jar PATH_TO_STANFORD_TAGGER_JAR --prop PATH_TO_PROP_FILE --model PATH_TO_MODEL_FILE
            --train PATH_TO_TRAIN_FILE

        example: python3 pos_stanford_train.py --jar StanfordTagger/stanford-postagger.jar --prop StanfordTagger/standfordPropsFile.prop
                   --model StanfordTagger/Stanford1 --train A3DataCleaned/Domain1Train.txt

        Note: to train egw4-reut.512.clusters file will be needed and its path needs to be set correctly in 'arch' property of
            stanfordPropsFile.prop file and also the 'arch' property needs to be set properly for different models to get maximum accuracy
