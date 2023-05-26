# pyOTTR - Reasonable Ontology Templates in Python

A Python module to help you convert your tabular data, like CSV, or Excel files, into [Resource Description Framework (RDF)](https://en.wikipedia.org/wiki/Resource_Description_Framework) triples. 

You can skip ahead to [an example](#example) or [usage instructions](#usage) if you already know what RDF and OTTR are. 
But if you are unsure, let me give you some context before I tell you more about the project itself.  

&nbsp;
## Introduction

The [Resource Description Framework (RDF)](https://www.w3.org/RDF/) is one of the [W3C Open Web Standards](https://www.w3.org/standards/). 
It is a flexible data model underpinning the [Semantic Web](https://www.w3.org/standards/semanticweb/). From [w3.org/RDF]:

>RDF is a standard model for data interchange on the Web. RDF has features that facilitate data merging even if the underlying schemas differ, and it specifically supports the evolution of schemas over time without requiring all the data consumers to be changed.
>
>RDF extends the linking structure of the Web to use URIs to name the relationship between things as well as the two ends of the link (this is usually referred to as a "triple"). Using this simple model, it allows structured and semi-structured data to be mixed, exposed, and shared across different applications.

[Linke Data](https://www.w3.org/standards/semanticweb/data) is information on the Web expressed as a graph, in a common standard, like the RDF. 
It promotes data interoperability and integration since it uses globally unique identifiers (URIs) and shared vocabularies to denote concepts, enabling different datasets to "speak the same language". 
It makes data more meaningful, opening up new possibilities for interoperability, discovery, reusability, and [collaboration without coordination](https://www.youtube.com/watch?v=ytedBJUx6bA). 

RDF offers several compelling advantages compared to data locked in tabular formats like CSV, spreadsheets or tables in relational database systems. 
I am convinced, but why would you trust me? 
What if you wanted to try it yourself on data that makes sense to you?

Here is the problem. 
Most of our information is locked in simple tabular forms, and converting it to RDF statements is cumbersome and error-prone at best. 

[Reasonable Ontology Templates (OTTR)](https://ottr.xyz/) offers a solution. 
If writing RDF by hand is like [assemby programming](https://en.wikipedia.org/wiki/Assembly_language), OTTR is like switching to [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), but for ontology modelling. (At least according to OTTR creators). 

Terse Syntax for Reasonable Ontology Templates (stOTTR)](https://dev.spec.ottr.xyz/stOTTR/) allows us to define templates which can then be used to reliably translate it to RDF. If you want to know about the motivation behind it, to really understand why, read [the presentation by OTTR creators](https://www.uio.no/studier/emner/matnat/ifi/IN3060/v19/undervisningsmateriale/ottr-part1.pdf) from the University of Oslo, or at watch the [Motivation and Overview presentation](https://ottr.xyz/#Presentation:_Motivation_and_Overview).

&nbsp;
## Example

Probably the most common example in the world of ontologies is that of a named pizza!. 
I will copy here the example from the [OTTR page](https://ottr.xyz/#Presentation:_Motivation_and_Overview).
We can represent named pizzas in a CSV file named `pizzas.csv` like so: 

```csv
name
Margherita
Hawaii
Grandiosa
```

We know that Margherita, Hawaii and Grandiosa are pizza names, because the first piece of information is `name` and the file is called `pizzas`. We can econde the same information in an RDF file `my.rdf` like so:

```rdf
p:Margherita rdf:type owl:Class .
p:Margherita rdfs:subClassOf p:Pizza .
p:Margherita rdfs:label "Margherita" .

p:Hawaii rdf:type owl:Class .
p:Hawaii rdfs:subClassOf p:Pizza .
p:Hawaii rdfs:label "Hawaii" .

p:Grandiosa rdf:type owl:Class .
p:Grandiosa rdfs:subClassOf p:Pizza .
p:Grandiosa rdfs:label "Grandiosa" .
```

But with just a few instances it is a lot of typing, many opportunities for errors. So instead, we can wrte two stOTTR templates in a `pizzas.stottr`.

```stottr
ax:SubClassOf [ ?sub, ?super ] :: {
    ottr:Triple(?sub, rdfs:subClassOf, ?super)
} .

pz:Pizza [ ?identifier, ?label ] :: {
    ottr:Triple(?identifier, rdf:type, owl:Class),
    ax:SubClassOf(?identifier, p:Pizza),
    ottr:Triple(?identifier, rdfs:label, ?label)
} .
```

With this definition we can invoke instances of the `pz:Pizza` templates, perhaps further down in the file. 

```stottr
pz:Pizza(p:Margherita, "Margherita") .
pz:Pizza(p:Hawaii, "Hawaii") .
pz:Pizza(p:Grandiosa, "Grandiosa") .
```

The above will produce the exact RDF example as above with less chance of a typo or other mistake. 

But we want to take it a step further. We already have the information in `pizzas.csv` and the stottr template in `pizzeria.stottr`. Now, let's use python to generate the RDF. 

```python
ottr = PyOTTR("pizzeria.stottr")

with open("pizzas.csv", "r") as data:
    for pizza in csv.DictReader(data):
        name = pizza["name"].strip()
        print(ottr.expand("pz:Pizza", f"p:{name}", name))
```

Or even simpler, if the column names and variable names are aligned:

```python
PyOTTR("pizzeria.stottr").expand("pizzas.csv").into("pz:Pizza")
```
&nbsp;
## Usage

At the moment the project is in early stages of development, so you cannot use it just yet. 
However, the idea is that you will be able to run it either as a script or a library from inside your project. 
It will not do everything the reference implementation - [Lutra](https://gitlab.com/ottr/lutra/lutra) - does. The focus is on translating CSV and [CSVW](https://csvw.org/standards.html) files, or data available as python objects, arrays or dictionaries. 

Currently, the work is focused on `stOTTR` implementation. The `tabOTTR` is likely the next step followed by potentially a new OTTR flavour to deal with CSVW. 

If you cannot wait, you can always help to get it done. It's an open-source project after all!

&nbsp;
## Contributing

Starts and pull requests are welcomed as are any ideas and comments. 
To test the project after cloning do `pytest`. After making any changes do `make style` to run _isort_, _flake8_ and _black_ on code which is not autogenerated. 

If the ANTLR grammar has to be updated (due to changes to the specification) you will have to
* Download a new grammar file and save it as `antlr/stOTTR.g4`.
* Enusre there is `turtleDoc : directive*;` line as a first rule in `Turtle.g4`.
* To build the grammar lexers and parsers in `pyottr/grammar` by invoking `make grammar`.

## Resources

* To learn about ANTLR, see [the mega tutorial](https://tomassetti.me/antlr-mega-tutorial) by Gabriele Tomassetti.
* [Lutra stOTTR parser tests](https://github.com/rtto/lutra-mirror/blob/develop/lutra-stottr/src/test/java/xyz/ottr/lutra/stottr/parser/ParserTest.java) have example of usage and what needs to be covered. 
* [Lutra model](https://github.com/rtto/lutra-mirror/tree/develop/lutra-core/src/main/java/xyz/ottr/lutra/model). 