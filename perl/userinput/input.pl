#! /usr/bin/env perl

use strict;
use warnings;

my $color;

print("What's your favorite color? ");
chomp($color = <STDIN>);
print("Your favorite color is $color\n");
