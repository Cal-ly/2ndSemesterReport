using System;
using System.IO;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string filePath = "path_to_your_file.txt";  // Path to the file containing postal codes and city names
        var lines = File.ReadAllLines(filePath);
        Console.WriteLine("public static readonly Dictionary<string, string> PostalCodeToCity = new Dictionary<string, string>");
        Console.WriteLine("{");

        foreach (var line in lines)
        {
            var parts = line.Split(new[] {'\t'}, StringSplitOptions.RemoveEmptyEntries);
            if (parts.Length >= 2)
            {
                string postalCode = parts[0].Trim();
                string cityName = parts[1].Trim();
                Console.WriteLine($"    {{\"{postalCode}\", \"{cityName}\"}},");
            }
        }

        Console.WriteLine("};");
    }
}