#!/usr/bin/env python3
import abc


class TransformCapability(abc.ABC):
    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self) -> str:
        pass
