Team Members:
    Arnob Mallik (CCID: amallik)
    Arif Hasnat (CCID: hasnat)


INSTALL:

pip3 install dill

Execution Instructions for Testing:
    To test using stanford pos tagger, run following command from command line:
        python3 pos_stanford_test.py --jar PATH_TO_STANFORD_TAGGER_JAR --model PATH_TO_MODEL_FILE --test PATH_TO_TEST_FILE

        example: python3 pos_stanford_train.py --jar StanfordTagger/stanford-postagger.jar --model StanfordTagger/Stanford1
                    --test A3DataCleaned/Domain1Test.txt


	To test using nltk (hmm, brill), run following command from command line:
        python3 pos_nltk_test.py --model PATH_TO_MODEL_FILE --test PATH_TO_TEST_FILE

        example: python3 pos_nltk_test.py --model models/hmm1 --test A3DataCleaned/Domain1Test.txt
		example: python3 pos_nltk_test.py --model models/brill1_base_hmm --test A3DataCleaned/Domain1Test.txt
		

Execution Instructions for Testing:		
	To train using stanford pos tagger, run following command from command line:
        python3 pos_stanford_train.py --jar PATH_TO_STANFORD_TAGGER_JAR --prop PATH_TO_PROP_FILE --model PATH_TO_MODEL_FILE
            --train PATH_TO_TRAIN_FILE

        example: python3 pos_stanford_train.py --jar StanfordTagger/stanford-postagger.jar --prop StanfordTagger/standfordPropsFile.prop
                   --model StanfordTagger/Stanford1 --train A3DataCleaned/Domain1Train.txt

        Note: to train egw4-reut.512.clusters file will be needed and its path needs to be set correctly in 'arch' property of
            stanfordPropsFile.prop file
			Model will be saved in PATH_TO_MODEL_FILE
	

    To train using nltk hmm, run following command from command line:
        python3 pos_hmm_train.py --model PATH_TO_MODEL_FILE --train PATH_TO_TRAIN_FILE

        example: python3 pos_hmm_train.py --model models/hmm1 --train A3DataCleaned/Domain1Train.txt

        Note: Model will be saved in PATH_TO_MODEL_FILE
		
		
	To train using nltk brill base hmm, run following command from command line:
        python3 pos_brill_hmm_train.py --model PATH_TO_MODEL_FILE --train PATH_TO_TRAIN_FILE

        example: python3 pos_brill_hmm_train.py --model models/brill1_base_hmm --train A3DataCleaned/Domain1Train.txt

        Note: Model will be saved in PATH_TO_MODEL_FILE
		