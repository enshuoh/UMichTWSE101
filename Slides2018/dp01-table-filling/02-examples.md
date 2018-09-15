## Dynamic Programming Examples

String Problems  
Classical String Problems  
Fancy String Problems

--

<!-- .slide: data-background="#FDA" -->
### Disclaimer

* ![](https://i.kym-cdn.com/entries/icons/original/000/016/739/Screen_Shot_2014-10-27_at_3.58.12_PM.png)<!-- .element: style="float:right;width:20%" -->
We have 10 examples in the slides, but we will go through only 10 examples today (at base-$k$).
* Please keep this in mind: <!-- .element: class="fragment" -->
    * To <b><i>feel</i></b> about how dynamic programming works.
    * The idea for coming up recurrence relations, and where do <b><i>subproblems</i></b> come from.

---

### Text Similarity

* Given two strings $A, B$, we want to measure <b><i>how similar</i></b> they are. There are several ways to define similarity (e.g., `${\textrm{LCS}}(A, B)$`, `${\textrm{EDIT-DIST}}(A, B)$`).

--

### Longest Common Subsequence

* Given two strings $A\in \Sigma^n$ and $B\in \Sigma^m$. Find a longest string that appears in both $A$ and $B$ as subsequences.

* Example:
    * `$A = $` `ALGORITHM` <!-- .element: id="LCS-example-A" -->
    * `$B = $` `ALTRUISTIC` <!-- .element: id="LCS-example-B" -->
    * <!-- .element: class="fragment" data-tmt="LCS-example" --> `${\rm{LCS}}(A, B) =$ ALRIT` 

--

### Observation

* Let us focus on the last character of each string:
    ![](https://hips.hearstapps.com/ghk.h-cdn.co/assets/cm/15/11/480x552/54ff047186bb0-ghk-iceberg-lettuce-xl.jpg?resize=*:2277) <!-- .element: style="float:right;width:15%" -->
    - If they are <span style="color:blue"><b><i>different</i></b></span>, then LCS cannot contain both characters.
    - If they are <span style="color:blue"><b><i>the same</i></b></span>, then one of the possible LCS *could* contain this character at the end.

--

### Recurrence Relation

* <!-- .element: style="font-size:80%" --> Let `$OPT(A, B) := |{\rm{LCS}}(A, B)|$`. Then,

* <!-- .element: style="font-size:80%" -->
`$OPT(a_1\cdots a_n, b_1\cdots b_m)$`
 `$= \begin{cases}
\max\left\{
    \begin{array}{l}
    OPT(a_1\cdots a_n, b_1\cdots b_{m-1}) \\
    OPT(a_1\cdots a_{n-1}, b_1\cdots b_{m})
    \end{array}
    \right\} & \text{if $a_n\neq b_m$,} \\
\max\left\{
    \begin{array}{l}
    OPT(a_1\cdots a_{n-1}, b_1\cdots b_{m-1}) + 1 \\
    OPT(a_1\cdots a_n, b_1\cdots b_{m-1}) \\
    OPT(a_1\cdots a_{n-1}, b_1\cdots b_{m})
    \end{array}
    \right\} & \text{if $a_n = b_m$.}
\end{cases}.
$` 

* <!-- .element: style="font-size:80%;color:brown" class="fragment" -->
Is there a simpler way to represent strings in the subproblems?

--

### Recurrence Relation

* <!-- .element: style="font-size:80%" --> Let `$OPT(i, j) := |{\rm{LCS}}(a_1\cdots a_i, b_1\cdots b_j)|$`. Then,

* <!-- .element: style="font-size:80%" -->
`$OPT(n, m)$`
 `$= \begin{cases}
\max\left\{
    \begin{array}{l}
    OPT(n, m-1) \\
    OPT(n-1, m)
    \end{array}
    \right\} & \text{if $a_n\neq b_m$,} \\
\max\left\{
    \begin{array}{l}
    OPT(n-1, m-1) + 1 \\
    OPT(n, m-1) \\
    OPT(n-1, m)
    \end{array}
    \right\} & \text{if $a_n = b_m$.}
\end{cases}.
$` 

* <!-- .element: style="font-size:80%;color:brown" class="fragment" -->
What are base cases?

* <!-- .element: style="font-size:80%;color:brown" class="fragment" -->
`$OPT(n, m) = 0$` when $n=0$ or $m=0$.

--

### It's Just Table Filling!

|   | A | L | G | O | R | I | T | H | M |
|:-----:|---|---|---|---|---|---|---|---|---|
| A | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| L | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| T | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| R | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 |
| U | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 |
| I | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 4 |
| S | 1 | 2 | 2 | 2 | 3 | 4 | 4 | 4 | 4 |
| T | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 5 | 5 |
| I | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 5 | 5 |
| C | 1 | 2 | 2 | 2 | 3 | 4 | 5 | 5 | 5 ||
<!-- .element: style="font-size:70%;" class="tmt plain-table" id="LCS-example-table" -->

--

### Extract LCS from OPT.

---

### Edit Distance

* You have two strings `$A\in \Sigma^n$` and `$B\in \Sigma^m$`. You would like to transform `$A$` to `$B$` via character
<span style="color:blue"><i>insertions</i></span>,
<span style="color:red"><i>deletions</i></span>
and 
<span style="color:darkgreen"><i>swaps</i></span>.
* We can visualize text similarity by <b><i>alignments</i></b>.

--

### Alignments

| | | | | | | | | | | | |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `$A$`: | A | L |<!-- .element: class="ed-swap" --> G |<!-- .element: class="ed-del" --> O | R |<!-- .element: class="ed-ins" -->   | I |<!-- .element: class="ed-ins" -->   | T |<!-- .element: class="ed-swap" --> H |<!-- .element: class="ed-swap" --> M |
| `$B$`: | A | L |<!-- .element: class="ed-swap" --> T |<!-- .element: class="ed-del" -->   | R |<!-- .element: class="ed-ins" --> U | I |<!-- .element: class="ed-ins" --> S | T |<!-- .element: class="ed-swap" --> I |<!-- .element: class="ed-swap" --> C |
| | | | | | | | | | | | | |

* `${\textrm{EDIT-DIST}}$` parameterized by three numbers:
    * `$c_i$`: cost to <span class="ed-ins">insert</span> character
    * `$c_s$`: cost to <span class="ed-swap">swap</span> character with another
    * `$c_d$`: cost to <span class="ed-del">delete</span> character

**Exercise**: Write out the recurrence relation.

---

### Longest Palindromic Subsequence

* We say that a string `$S$` is a 
<b><i>palindrome</i></b>
if `$S$` equals to reverse$(S)$.
* You are given a string $A\in\Sigma^n$. Find a longest subsequence of $A$ that is a palindrome.
* Example: `ABRACADABRA`

--

#### (Just for fun) An Interesting Result.

$|{\textrm{LPS}}(A)| = |{\textrm{LCS}}(A, {\textrm{reverse}}(A))|$.

---

### Typesetting Problem

* <div class="typesetting-example">
Assuming we are living in a world with no punctuations. You are given a paragraph of $n$ words, the $i$-th word has length $w_i$.
    </div>
* <div class="typesetting-example"> Now, we want to print the paragraph on a paper of width $W$. In each line, there should be exactly one space between neighboring words. However, there are leftover spaces, with its size denoted by $\ell_j$ for $j$-th line (except the last line).
    </div>
* <div class="typesetting-example">The <b><i>uglyness</i></b> is defined by $\sum\ell_j^3$. Can you find a way to print the paragraph minimizing the cost?
    </div>

--

### Longest Valid Parenthesis Subsequence

* You are given a sequence of parenthesis

--

### Longest Common Subsequence Multiple Patterns

--

### String Compression

--

### Painting a Long String

--

### Assembling Words

--

### Longest Palindromic Substring

