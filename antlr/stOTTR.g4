/*** stOTTR grammar from https://dev.spec.ottr.xyz/stOTTR/index.html ***/

grammar Stottr;

import Turtle;


stOTTRDoc
 : ( directive // Turtle prefixes and base
   | statement )* EOF
 ;

statement
 : ( signature
     | template
     | baseTemplate
     | instance
   )
 '.'
 ;


/*** Comments ***/

Comment
 : '#' ~('\r' | '\n')* -> skip
 ;

CommentBlock
 : '/***' .*? '***/' -> skip
 ;


/*** Signature ***/

signature
 : templateName parameterList annotationList?
 ;

templateName
 : iri
 ;

parameterList
 : '[' (parameter (',' parameter)*)? ']'
 ;

parameter
 : ParameterMode* type? Variable defaultValue?
 ;

ParameterMode
 : '?'  /* optional */
 | '!'  /* non blank */
 ;

defaultValue
 : '=' constantTerm
 ;

annotationList
 : (annotation ','?)*
 ;

annotation
 : '@@' instance
 ;


/*** Templates ***/

baseTemplate
 : signature '::' 'BASE'
 ;

template
 : signature '::' patternList
 ;

patternList
 : '{' (instance ','?)* '}'
 ;


/*** Instance ***/

instance
 : (ListExpander '|')? templateName argumentList
 ;

ListExpander
 : 'cross'
 | 'zipMin'
 | 'zipMax'
 ;

argumentList
 : '(' (argument (',' argument)*)? ')'
 ;

argument
 : ListExpand? term 
 ;

ListExpand
 : '++'
 ;


/*** Types ***/

type
 : basicType
 | lubType
 | listType
 | neListType
 ;

listType
 : 'List<' type '>'
 ;

neListType
 : 'NEList<' type '>'
 ;

lubType
 : 'LUB<' basicType '>'
 ;

basicType
 : prefixedName
 ;


/*** Terms ***/

term
 : Variable
 | constant
 | termList
 ;

constantTerm
 : constant
 | constantList
 ;

Variable
 : '?' BNodeLabel
 ;

/* Turtle blank node labels without trailing '_:' */
fragment BNodeLabel
 : (PN_CHARS_U) ((PN_CHARS | '.')* PN_CHARS)?
 ;

constant
 : iri
 | blankNode
 | literal
 | none
 ;

none
 : 'none'
 ;

termList
 : '(' (term (',' term)*)? ')'
 ;

constantList
 : '(' (constantTerm (',' constantTerm)*)? ')'
 ;
