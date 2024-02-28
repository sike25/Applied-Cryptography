Fake Transactions
=================

The encrypted records can be segmented based on the field sizes known from the format:

	dc75d21c ae 71a1fbba62ec 52 ee48ac8f667e ea 75941d3b78f2bc
	dc75d218 ae 73a7fdb464e0 52 e848ac816673 ea 75941d3a7df7bc
	dc75d11e ae 72a4f6b465ef 52 e94aa9836572 ea 75941d3b79f4bc

We can make some immediate observations:
- All encrypted transaction numbers have the same 2 leading bytes (`dc 75`). We suspect that transaction numbers are small and they probably start with 2 leading 0s (00).
- Similarly, all encrypted amounts start with the same 3 leading bytes (`75 94 1d`). We suspect that amounts  are small and these are leading 0's.
- No repeating IDs appear in the same role (all source account IDs are different and all destination account IDs are different, too).

Since all records are encrypted with the same key stream, we can XOR the same field from different records: the key stream bytes will cancel out and we obtain the XOR sum of the plaintext fields ((F + K) + (F’ + K) = F + F’). We may use this to figure out the destination account IDs in each record.

For instance, we can first compute the XOR sum of the known account IDs (for all 5-choose-2 = 10 pairs). Then we can  XOR the destination IDs in record 1 and 2, and check which of the previously computed values it matches. This gives possibilities for the actual destination IDs used in transaction 1 and 2...

For modifying an encrypted transaction record, recall that anything you XOR to it, will be XORed to the plaintext after decryption!

- A74635
- B29846
- C12859
- D37465
- E12654
