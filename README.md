# wikipedia
Projet Genie Logiciel Python

## The project
The goal of this project is to convert Wikipedia tables into the CSV format. Essentially we want a function that takes the URL of a Wikipedia page and saves all relevant tables to the CSV format.

## Running the App
To use our App, you need to respect these following steps :
1. Creating a virtual environment:
```
conda create -n envname python=3.9
```
```
conda activate envname
```
2. Installing dependencies:
```
pip install -r requirements.txt
```
3. Running the App:
```
python main/main.py
```

4. Testing:
```
pytest -q test/TestExtractor.py
```
```
pytest -q test/TestConvertor.py
```
```
pytest -q test/TestSerializer.py
```
## Challenges

Converting Wikipedia tables from HTML to CSV format is not an easy task, as choices and compromises as been made.

### First view of the problem

In order to access the HTML content of Wikipedia pages, we used Jsoup. This package allows an easy way to navigate in the DOM.
However, HTML tables are way more versatile than the CSV format can afford. View the example bellow

<table>
<tr>
<td></td>
<td><center>HTML</center></td>
<td><center>Into</center></td>
<td><center>CSV</center></td>
</tr>
<tr>
<td>Code</td>
<td>

```                             
<table class="wikitable">       
    <tr>                        
        <td>a</td>              
        <td>b</td>              
        <td>c</td>              
    </tr>                       
    <tr>                        
        <td>d</td>              
        <td colspan=2>e</td>    
    </tr>                       
</table>                        
```  

</td>

<td rowspan="2"> <font size="20">→<font></td>

<td>
<center>
    "a","b","c"<br>
    "d","e","e"
</center>
</td>

</tr>
<tr>
<td>Render</td>
<td>
<center>
<table class="wikitable">       
    <tr>                        
        <td>a</td>              
        <td>b</td>              
        <td>c</td>              
    </tr>                       
    <tr>                        
        <td>d</td>              
        <td colspan="2"><center>e</center></td>    
    </tr>                       
</table>   
</center>
</td>

<td>
<center>
<table class="wikitable">       
    <tr>                        
        <td>a</td>              
        <td>b</td>              
        <td>c</td>              
    </tr>                       
    <tr>                        
        <td>d</td>              
        <td>e</td>    
        <td>e</td>
    </tr>                       
</table>   
</center>
</td>
</tr>
</table>  

As we can see, the cell named "e" is duplicated in the CSV form. In fact, the multicell can't be represented in CSV. We made the choice to just duplicate the value.
HTML tables can be very tricky as you can see on the [Help table](https://en.wikipedia.org/wiki/Help:Table) web page of Wikipedia.
Cells can span multiple rows and/or columns. Also, tables can be nested as far as we want. So one cell can have a table in it, and this cell can span multiple cells. This situation cannot be represented in CSV like in HTML. So we choose to duplicate rows and columns in order to have the space to fit the data and keep links between rows and columns. An example of the situation of a nested table is given below:

<table>
<tr>
<td></td>
<td><center>HTML</center></td>
<td><center>Into</center></td>
<td><center>CSV</center></td>
</tr>
<tr>
<td>Code</td>
<td>

```                             
<table class="wikitable">
    <tr>
        <td>a</td>
        <td>b</td>
        <td>c</td>
    </tr>
    <tr>
        <td>e</td>
        <td>f</td>
        <td>g</td>
    </tr>
    <tr>
        <td>d</td>
        <td colspan=2>
            <table class="wikitable">
                <tr>
                    <td>a1</td>
                    <td>b1</td>
                </tr>
                <tr>
                    <td colspan=2>c1</td>
                </tr>
            </table>
        </td>
    </tr>
</table>                     
```  

</td>

<td rowspan="2"> <font size="20">→<font></td>

<td>
<center>
    "a","b","b","c","c"<br>
    "e","f","f","g","g"<br>
    "d","a1","a1","b1","b1"<br>
    "d","c1","c1","c1","c1"
</center>
</td>

</tr>
<tr>
<td>Render</td>
<td>
<center>
<table class="wikitable">
    <tr>
        <td>a</td>
        <td>b</td>
        <td>c</td>
    </tr>
    <tr>
        <td>e</td>
        <td>f</td>
        <td>g</td>
    </tr>
    <tr>
        <td>d</td>
        <td colspan=2>
            <table class="wikitable">
                <tr>
                    <td>a1</td>
                    <td>b1</td>
                </tr>
                <tr>
                    <td colspan=2>c1</td>
                </tr>
            </table>
        </td>
    </tr>
</table>
</center>
</td>

<td>
<center>
<table class="wikitable">       
    <tr>                        
        <td>a</td>              
        <td>b</td>
        <td>b</td>              
        <td>c</td>  
        <td>c</td>              
    </tr>
    <tr>                        
        <td>e</td>              
        <td>f</td>
        <td>f</td>              
        <td>g</td>  
        <td>g</td>              
    </tr>
    <tr>                        
        <td>d</td>              
        <td>a1</td>
        <td>a1</td>              
        <td>b1</td>  
        <td>b1</td>              
    </tr>
    <tr>                        
        <td>d</td>              
        <td>c1</td>
        <td>c1</td>              
        <td>c1</td>  
        <td>c1</td>              
    </tr>                                        
</table>   
</center>
</td>
</tr>
</table>

So we flatten tables in order to convert them into CSV. This flattening is performed from the bottom up so that no matter how many nested tables there are, all data will be present in the right place.

Moreover, as you can see at [Help table](https://en.wikipedia.org/wiki/Help:Table), tables can contain different types of data. They can be images, videos, links, or any other HTML content. In this project, we focused on making a modular application that can evolve to take into account more tables and data. In this view, we already implemented the support for "text", "links" and "images". Those types need to be converted to text somehow in order to fit CSV files. For "links" we take the "href" attribute and for "images" the "src" one that we append to the text. This behavior can easily be changed.  

## Architecture
The architecture of this app is <b>three</b> main parts:

1. The EXTRACTOR take the URL of a Wikipedia page and output table elements with all their respective children.

2. The CONVERTOR takes a table or a list of tables and outputs them as a table of string.

3. The SERIALIZER saves string tables into CSV files at the default or wanted location.
