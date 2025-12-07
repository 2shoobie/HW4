This data refers to the grades of student exams. It shows their gender race/ethnicity, and test prerpations and reading and writing scores as a student. It carries over 1000 rows of data. I went ahead and loaded up
the file into the python using pandas. To analyze the first rows, type of columns and simple statistcs, I used the following functions in the analysis: Info & Describe.
Iloc and loc were used to retrieve single rows, pieces of rows, a column and a particular cell. I created two filters, the one that identifies the students achieving high marks in reading and the other filter 
is used to identify male students achieving low marks in reading. Another column I also created is the mean score in math, reading and writing. Then I went ahead and column drop() the reading score. 
Finally, I applied groupby in order to determine the mean writing score of each gender. Based on the figures I observed that average math, reading, and writing results are near to one another. 
There were students with extremely high scores of nearly 100 and those with extremely low scores. Numerous of the students who received a score of above 90 in reading also scored highly in writing. 
The data appear to be complete without any missing values. One bizarre problem is that gender is small in the file and hence the filtering should be an exact match. 
Generally speaking, the data is clean and simple to handle.
