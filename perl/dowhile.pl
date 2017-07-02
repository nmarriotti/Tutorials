#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';

say("Hello World");

my $i = 0;

do {
	say $i;
	$i += 1;
} while ($i < 10);
