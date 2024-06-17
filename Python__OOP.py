{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNnA2gowupgaT3OEErFo/cC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ducanhngo/AIO_2024_087_AnhDuc/blob/feature%2Fexercise/Python__OOP.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 1"
      ],
      "metadata": {
        "id": "kvs8KJBMtxgt"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IXPlcxarW9d2",
        "outputId": "221793a6-b528-4026-ad3c-b946d5b06533"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([0.0900, 0.2447, 0.6652])"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ],
      "source": [
        "import torch\n",
        "import torch.nn as nn\n",
        "data = torch.Tensor([1,2,3])\n",
        "softmax_function = nn.Softmax(dim=0)\n",
        "output = softmax_function(data)\n",
        "output"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 2"
      ],
      "metadata": {
        "id": "WxFWWZnst_52"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import torch\n",
        "import torch.nn as nn\n",
        "\n",
        "class My_Softmax(nn.Module):\n",
        "  def __init__(self):\n",
        "    super().__init__()\n",
        "  def forward(self, x):\n",
        "    return torch.exp(x)/torch.sum(torch.exp(x))\n",
        "data = torch.Tensor([5 , 2 , 4])\n",
        "my_softmax = My_Softmax()\n",
        "output = my_softmax(data)\n",
        "print(output)"
      ],
      "metadata": {
        "id": "tw9wGrJ4t3T0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e4f4e2fa-075e-4bf8-9484-cfe1931850e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "tensor([0.7054, 0.0351, 0.2595])\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 3\n"
      ],
      "metadata": {
        "id": "MLZDymhcvJtN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import torch\n",
        "import torch.nn as nn\n",
        "\n",
        "class My_Softmax(nn.Module):\n",
        "  def __init__(self):\n",
        "    super().__init__()\n",
        "  def forward(self, x):\n",
        "    return torch.exp(x)/torch.sum(torch.exp(x))\n",
        "data = torch.Tensor([1, 2, 300000000])\n",
        "my_softmax = My_Softmax()\n",
        "output = my_softmax(data)\n",
        "print(output)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kaJauR9JvMl_",
        "outputId": "bd72bab2-4e56-4384-9977-e8e8b23a1e3a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "tensor([0., 0., nan])\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 4"
      ],
      "metadata": {
        "id": "1NalaNRLzJtw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import torch\n",
        "import torch.nn as nn\n",
        "\n",
        "class Softmax_Stable(nn.Module):\n",
        "  def __init__(self):\n",
        "    super().__init__()\n",
        "  def forward(self, x):\n",
        "    x_max = torch.max(x, dim = 0, keepdims = True)\n",
        "    x_exp = torch.exp(x - x_max.values)\n",
        "    partition = x_exp.sum(0, keepdim = True)\n",
        "    return x_exp/partition\n",
        "data = torch.Tensor([1,2,3])\n",
        "my_softmax = Softmax_Stable()\n",
        "output = my_softmax(data)\n",
        "print(output)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KzYpBv2FzM6w",
        "outputId": "c6df7c1d-98c9-47a5-e076-b4c9482f2943"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "tensor([0.0900, 0.2447, 0.6652])\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 5:"
      ],
      "metadata": {
        "id": "li8iQDblxmHr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from abc import ABC, abstractmethod\n",
        "\n",
        "class Person(ABC):\n",
        "  def __init__(self, name: str, yob: int):\n",
        "    self._name = name\n",
        "    self._yob = yob\n",
        "    def get_yob(self):\n",
        "      return self._yob\n",
        "    @abstractmethod\n",
        "    def describe(self):\n",
        "      pass\n",
        "class Student(Person):\n",
        "  def __init__(self,name: str, yob: int, grade: str):\n",
        "    self._name = name\n",
        "    self._yob = yob\n",
        "    self._grade = grade\n",
        "  def describe(self):\n",
        "    print(f\"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}\")\n",
        "\n",
        "student1 = Student(name =\"studentZ2023\", yob =2011 , grade =\"6\")\n",
        "student1.describe()"
      ],
      "metadata": {
        "id": "JMe-DWKbq3IQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "02da6b91-3b4c-4e3b-fcd1-63499f691bf8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Student - Name:  studentZ2023  - YoB: 2011 - Grade: 6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "#Question 6:\n"
      ],
      "metadata": {
        "id": "6k6vNGRV0vG2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from abc import ABC, abstractmethod\n",
        "\n",
        "class Person(ABC):\n",
        "  def __init__(self, name: str, yob: int):\n",
        "    self._name = name\n",
        "    self._yob = yob\n",
        "    def get_yob(self):\n",
        "      return self._yob\n",
        "class Teacher(Person):\n",
        "  def __init__(self,name: str, yob: int, subject: str):\n",
        "    self._name = name\n",
        "    self._yob = yob\n",
        "    self._subject = subject\n",
        "  def describe(self):\n",
        "    print(f\"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}\")\n",
        "\n",
        "teacher1 = Teacher(name =\"teacherZ2023\", yob =1991 , subject =\"History\")\n",
        "teacher1.describe()"
      ],
      "metadata": {
        "id": "EH5Qj6LQ004Z",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "70efdd9c-2833-446b-ed35-038fc30e157c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Teacher - Name:  teacherZ2023  - YoB: 1991 - Subject:  History \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 7"
      ],
      "metadata": {
        "id": "IjJ7Nwj6XWA6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from abc import ABC, abstractmethod\n",
        "\n",
        "class Person(ABC):\n",
        "  def __init__(self, name: str, yob: int):\n",
        "    self._name = name\n",
        "    self._yob = yob\n",
        "    def get_yob(self):\n",
        "      return self._yob\n",
        "class Doctor(Person):\n",
        "  def __init__(self,name: str, yob: int, specialist: str):\n",
        "    self._name = name\n",
        "    self._yob = yob\n",
        "    self._specialist = specialist\n",
        "  def describe(self):\n",
        "    print(f\"Teacher - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}\")\n",
        "\n",
        "doctor1 = Doctor ( name =\"doctorZ2023\", yob =1981 , specialist =\"Endocrinologists\")\n",
        "doctor1.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AocQN8paXXZq",
        "outputId": "637fbfe2-56d4-4403-edf2-f9cab7123428"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Teacher - Name: doctorZ2023 - YoB: 1981 - Specialist: Endocrinologists\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 8"
      ],
      "metadata": {
        "id": "wTo5g25bYei-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Person:\n",
        "    def __init__(self, name: str, yob: int):\n",
        "        self.name = name\n",
        "        self.yob = yob\n",
        "\n",
        "    def describe(self):\n",
        "        print(f\"Name: {self.name}, YoB: {self.yob}\")\n",
        "\n",
        "class Student(Person):\n",
        "    def __init__(self, name: str, yob: int, grade: str):\n",
        "        super().__init__(name, yob)\n",
        "        self.grade = grade\n",
        "\n",
        "    def describe(self):\n",
        "        print(f\"Student Name: {self.name}, YoB: {self.yob}, Grade: {self.grade}\")\n",
        "\n",
        "class Teacher(Person):\n",
        "    def __init__(self, name: str, yob: int, subject: str):\n",
        "        super().__init__(name, yob)\n",
        "        self.subject = subject\n",
        "\n",
        "    def describe(self):\n",
        "        print(f\"Teacher Name: {self.name}, YoB: {self.yob}, Subject: {self.subject}\")\n",
        "\n",
        "class Doctor(Person):\n",
        "    def __init__(self, name: str, yob: int, specialist: str):\n",
        "        super().__init__(name, yob)\n",
        "        self.specialist = specialist\n",
        "\n",
        "    def describe(self):\n",
        "        print(f\"Doctor Name: {self.name}, YoB: {self.yob}, Specialist: {self.specialist}\")\n",
        "\n",
        "class Ward:\n",
        "    def __init__(self, name: str):\n",
        "        self.__name = name\n",
        "        self.__listPeople = list()\n",
        "\n",
        "    def add_person(self, person: Person):\n",
        "        self.__listPeople.append(person)\n",
        "\n",
        "    def describe(self):\n",
        "        print(f\"Ward Name: {self.__name}\")\n",
        "        for p in self.__listPeople:\n",
        "            p.describe()\n",
        "\n",
        "    def count_doctor(self):\n",
        "        return sum(1 for person in self.__listPeople if isinstance(person, Doctor))\n",
        "\n",
        "student1 = Student(name=\"studentA\", yob=2010, grade=\"7\")\n",
        "teacher1 = Teacher(name=\"teacherA\", yob=1969, subject=\"Math\")\n",
        "teacher2 = Teacher(name=\"teacherB\", yob=1995, subject=\"History\")\n",
        "doctor1 = Doctor(name=\"doctorA\", yob=1945, specialist=\"Endocrinologists\")\n",
        "doctor2 = Doctor(name=\"doctorB\", yob=1975, specialist=\"Cardiologists\")\n",
        "\n",
        "ward1 = Ward(name=\"Ward1\")\n",
        "ward1.add_person(student1)\n",
        "ward1.add_person(teacher1)\n",
        "ward1.add_person(teacher2)\n",
        "ward1.add_person(doctor1)\n",
        "ward1.add_person(doctor2)\n",
        "\n",
        "print(ward1.count_doctor())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xUuPol6OYgQX",
        "outputId": "a450c970-38ae-4091-fc99-917ffa4ff71c"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 9"
      ],
      "metadata": {
        "id": "6d7fV3hcY7op"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class MyStack:\n",
        "    def __init__(self, capacity):\n",
        "        self.__capacity = capacity\n",
        "        self.__stack = []\n",
        "\n",
        "    def is_full(self):\n",
        "        return len(self.__stack) == self.__capacity\n",
        "\n",
        "    def push(self, value):\n",
        "        if not self.is_full():\n",
        "            self.__stack.append(value)\n",
        "\n",
        "stack1 = MyStack(capacity=5)\n",
        "stack1.push(1)\n",
        "assert stack1.is_full() == False\n",
        "stack1.push(2)\n",
        "print(stack1.is_full())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LyrKZ5V5Y9X6",
        "outputId": "c05bbc0e-509b-4e54-d9e3-ddf8ba2409a4"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 10"
      ],
      "metadata": {
        "id": "Z2cZi2jsZX-b"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class MyStack:\n",
        "    def __init__(self, capacity):\n",
        "        self.__capacity = capacity\n",
        "        self.__stack = []\n",
        "\n",
        "    def is_full(self):\n",
        "        return len(self.__stack) == self.__capacity\n",
        "\n",
        "    def push(self, value):\n",
        "        if not self.is_full():\n",
        "            self.__stack.append(value)\n",
        "\n",
        "    def top(self):\n",
        "        if self.__stack:\n",
        "            return self.__stack[-1]\n",
        "\n",
        "stack1 = MyStack(capacity=5)\n",
        "stack1.push(1)\n",
        "assert stack1.is_full() == False\n",
        "stack1.push(2)\n",
        "print(stack1.top())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MB8uXg_OZZrX",
        "outputId": "ec8eda89-911e-42f2-eb5c-a848652dbc3c"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 11"
      ],
      "metadata": {
        "id": "sIVHEr3janMc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class MyQueue:\n",
        "    def __init__(self, capacity):\n",
        "        self.__capacity = capacity\n",
        "        self.__queue = []\n",
        "\n",
        "    def is_full(self):\n",
        "        return len(self.__queue) == self.__capacity\n",
        "\n",
        "    def enqueue(self, value):\n",
        "        if not self.is_full():\n",
        "            self.__queue.append(value)\n",
        "\n",
        "queue1 = MyQueue(capacity=5)\n",
        "queue1.enqueue(1)\n",
        "assert queue1.is_full() == False\n",
        "queue1.enqueue(2)\n",
        "print(queue1.is_full())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rOaRiezdao02",
        "outputId": "5bc1c9b1-5da0-4710-ec5b-5acc5838c633"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 12"
      ],
      "metadata": {
        "id": "7Q8w52yNapVW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class MyQueue:\n",
        "    def __init__(self, capacity):\n",
        "        self.__capacity = capacity\n",
        "        self.__queue = []\n",
        "\n",
        "    def isEmpty(self):\n",
        "        return len(self.__queue) == 0\n",
        "\n",
        "    def is_full(self):\n",
        "        return len(self.__queue) == self.__capacity\n",
        "\n",
        "    def enqueue(self, value):\n",
        "        if not self.is_full():\n",
        "            self.__queue.append(value)\n",
        "\n",
        "    def front(self):\n",
        "        if not self.isEmpty():\n",
        "            return self.__queue[0]\n",
        "\n",
        "queue1 = MyQueue(capacity=5)\n",
        "queue1.enqueue(1)\n",
        "assert queue1.is_full() == False\n",
        "queue1.enqueue(2)\n",
        "print(queue1.front())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uXDTzGG7be4L",
        "outputId": "a812df2f-c464-4f20-90c3-81177849debb"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    }
  ]
}