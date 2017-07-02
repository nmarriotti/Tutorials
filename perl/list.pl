#!/usr/bin/perl

@people = qw(Nick Ted Nancy);
$list_length = @people;

print $list_length;

foreach $people (@people) {
    print "$people\n";
}
