#!/usr/bin/env python3

def word_frequencies(filename):
    
    
    
   ''' words = []
    count = {}
    
    with open(filename, 'r') as f:
        for line in f:
            splitting = line.split()
            stripper = [i.strip("""!"#$%&'()*,-./:;?@[]_""") for i in splitting ]
            for i in stripper:
                words.append(i)
          
            
    wordset = set(words)
    for i in wordset:
        wordCount = words.count(i)
        count[i] = wordCount
        
    return count    
         '''
         
         
   result = {}
   with open(filename) as in_file:
    
       for w in in_file.read().split():
           ws = w.strip("""!"#$%&'()*,-./:;?@[]_""")
        
            
           if ws not in result:
              result[ws] = 0
            
           result[ws] += 1
        
   return result   
         
         
    





         
def main():
    for word, count in word_frequencies("alice.txt").items():
        print(f"{word}\t{count}")
    

    if __name__ == "__main__":
        main()
