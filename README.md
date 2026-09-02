## AltaML - Abhishek Sharma Assessment

Review - This is an assessment presented by Abhishek Sharma given by AltaML. the task is split into different tasks, please find the solution to all the tasks within this folder 

``` C:\Users\sharm\Desktop\AltaML\src\altaml ```

## How to run

### Requirements - 

<li>Python 3.9.9</li> 
<li>UV</li>

To run the main demo please use the following command.
<pre><code>uv run python -m altaml.main</code></pre>

*Make sure you are in the right directory* 
```C:\Users\Desktop\AltaML - I am running from this directory```

To run Task 3
<pre><code>uv run python -m altaml.petShop</code></pre>

### To run tests
<li>cd src\altaml </li>
<li><pre><code>uv run python -m unittest discover -s tests -v</code></pre></li>

## Design Decisions
<li> None represents a no name pet</li>
<li> Cats and Dogs always are within a random age between 5 and 10 </li>
<li> Name history is stored in a separate list so old name doesn't get overwritten and new is appended to the list. </li>
<li> Every 5th speak of cat and dog increment the age</li>
<li> Data as mentioned in the pdf is fake, transactions happen via beginTran, commit, insert and rollback</li>
<li> SQL uses two tables as we have historical name data </li>



## File Strucutre
<li> src\altaml\cat.py</li>
<li> src\altaml\dog.py</li>
<li> src\altaml\data.py</li>
<li> src\altaml\main.py</li>
<li> src\altaml\petShop.py</li>
<li> src\altaml\tests\test.py</li>
<li> src\altaml\homework.sql</li>

## Known discrepancy 

In the pseudo code given it is mentioned to include "Connecting to database" for part 1 for the data.pseudo code file but it is not displayed in the output shared in the assessment pdf, I have included it in my approach, that is the only difference