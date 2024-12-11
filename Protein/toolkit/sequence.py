#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Sequence(object):
    def __init__(self, sequences, descriptions):
        if len(sequences) != len(descriptions):
            raise ValueError("The number of sequences must match the number of descriptions.")
        self.sequences = sequences
        self.descriptions = descriptions

    @classmethod
    def from_a3m(cls, a3m, max_depth=None):
        # a3m: a3m str
        sequences, descriptions = cls.parse_a3m(a3m)
        if ((max_depth is not None)
                and (0 < max_depth < len(sequences))):
            sequences = sequences[:max_depth]
            descriptions = descriptions[:max_depth]
        return cls(
            sequences=sequences,
            descriptions=descriptions
        )

    @staticmethod
    def sequence2a3m(descriptions, sequences):
        a3m_lines = []
        for desc, seq in zip(descriptions, sequences, strict=True):
            a3m_lines.append(f'>{desc}')
            a3m_lines.append(seq)
        return '\n'.join(a3m_lines) + '\n'

    @staticmethod
    def parse_a3m(fasta):
        sequences = []
        descriptions = []
        # 处理超过一行的长序列
        curr_sequence = []
        curr_description = None

        fasta = fasta.splitlines()
        for line in fasta:
            line = line.strip()
            if line.startswith('>'):
                if curr_sequence:
                    sequences.append("".join(curr_sequence))
                    descriptions.append(curr_description)
                    curr_sequence = []
                curr_description = line[1:]
            elif line:
                curr_sequence.append(line)

        if curr_sequence:
            sequences.append("".join(curr_sequence))
            descriptions.append(curr_description)
        return sequences, descriptions



