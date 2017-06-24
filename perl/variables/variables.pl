#! /usr/bin/env perl

use strict;
use warnings;

my $name = "Nick";
my $number = 1_000_000;

print("Hello, ", $name, "! How are you?\n");
print("Hello, $name! How are you?\n");
printf("Hello, %s! How are you?\n", $name);

print("Number is ", $number, "\n");
print("Number is $number\n");
printf("Number is %d\n", $number);