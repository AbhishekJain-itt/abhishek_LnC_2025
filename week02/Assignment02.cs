using System;

class SubarrayMeanCalculator
{
    static void Main()
    {
        var input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        int numberOfElements = input[0];
        int numberOfQueries = input[1];

        long[] array = Array.ConvertAll(Console.ReadLine().Split(), long.Parse);

        long[] prefixSum = new long[numberOfElements + 1];
        for (int i = 1; i <= numberOfElements; i++)
        {
            prefixSum[i] = prefixSum[i - 1] + array[i - 1];
        }

        for (int i = 0; i < numberOfQueries; i++)
        {
            var query = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int left = query[0];
            int right = query[1];

            long sum = prefixSum[right] - prefixSum[left - 1];
            long meanFloor = sum / (right - left + 1);

            Console.WriteLine(meanFloor);
        }
    }
}
