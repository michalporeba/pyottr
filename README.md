# A Python version of stOTTR

Any data, especially open data, is better served in a triple form. 

But a lot of it is locked in tabular format: relational databases, CSV files and so on. The [stOTTR - Terse Syntax for Reasonable Ontology Templates](https://dev.spec.ottr.xyz/stOTTR/) tries to help with this problem. 
It provides a method of tranforming tabular data into [Resource Description Framework (RDF)](https://www.w3.org/RDF/). It is part of OTTR which is:

>Reasonable Ontology Templates (OTTR) is a language with supporting tools for representing and instantiating RDF graph and OWL ontology modelling patterns. It is designed to improve the efficiency and quality of building, using, and maintaining knowledge bases.

## There are a few things you can do here

* To understand why, read [the presentation by OTTR creators](https://www.uio.no/studier/emner/matnat/ifi/IN3060/v19/undervisningsmateriale/ottr-part1.pdf) from the University of Oslo.
* To make it work add `turtleDoc : directive*;` as a first rule in `Turtle.g4`.
* To build the grammar lexers and parsers do `make grammar`.
* To test do `pytest` on the command line.
* To learn about ANTLR, see [the mega tutorial](https://tomassetti.me/antlr-mega-tutorial) by Gabriele Tomassetti.

## How to use it

At the moment the project is in early stages of development, so you cannot use it just yet. 
However, the idea is that you will be able to run it either as a script or a library from inside your project. 
It will not do everything the reference implementation - [Lutra](https://gitlab.com/ottr/lutra/lutra) - does. The focus is on translating CSV and [CSVW](https://csvw.org/standards.html) files, or data available as python objects, arrays or dictionaries. 

If you cannot wait, you can always help to get it done. It's an open-source project after all!

## Resources

* [Lutra stOTTR parser tests](https://github.com/rtto/lutra-mirror/blob/develop/lutra-stottr/src/test/java/xyz/ottr/lutra/stottr/parser/ParserTest.java) have example of usage and what needs to be covered. 
* [Lutra model](https://github.com/rtto/lutra-mirror/tree/develop/lutra-core/src/main/java/xyz/ottr/lutra/model). 

Antlr definition in `stottr.g4` from 
https://www.antlr.org/