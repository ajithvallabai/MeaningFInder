from PyDictionary import PyDictionary

if __name__ == "__main__":

    # Call PyDictionary class
    dc = PyDictionary()

    # Opening input file
    # read from a file line by line
    # Get meaning of each word
    wordsFile = open('words.txt', 'r')
    count = 0
    wordMeanCollector = {}
    # Using for loop
    for line in wordsFile:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        meaning = dc.meaning(line.strip())
        wordMeanCollector[count] = [line.strip(),meaning]
    # Closing file
    wordsFile.close()

    # open output file
    # Structure and write to file
    outputFile = open('output.txt', 'w')
    for each in wordMeanCollector:
        subjectDict = list(wordMeanCollector[each][1].keys())
        subjectList = [''.join(ele) for ele in subjectDict]
        MeaningDict = list(wordMeanCollector[each][1].values())
        MeaningList = [','.join(ele) for ele in MeaningDict]
        outputFile.write("%s - %s - %s \n" % (wordMeanCollector[each][0], ",".join(subjectList), MeaningList[0]))
    outputFile.close()
