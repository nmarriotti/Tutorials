#! /usr/bin/env perl

use strict;
use warnings;

my $color;

print("What's your favorite color? ");
$color = <STDIN>;
chomp $color;
print("Your favorite color is $color\n");