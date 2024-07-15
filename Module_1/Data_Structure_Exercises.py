{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPr4jkA1PmtAtvw/CfxnTgO",
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
        "<a href=\"https://colab.research.google.com/github/Ducanhngo/AIO_2024_087_AnhDuc/blob/feature%2Fexercise-week1/Data_Structure_Exercises.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IXPlcxarW9d2",
        "outputId": "a6d84d35-180e-47aa-9798-8eaabd3118a3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[5, 5, 5, 5, 10, 12, 33, 33]\n"
          ]
        }
      ],
      "source": [
        "def max_kernel(user, k ):\n",
        "  output = []\n",
        "  for i in range(len(user) - k +1):\n",
        "      ls = []\n",
        "      for x in user[i:i+k]:\n",
        "          ls.append(x)\n",
        "      output.append(max(ls))\n",
        "  return output\n",
        "\n",
        "num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]\n",
        "k = 3\n",
        "print(max_kernel(num_list, k))\n"
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
        "def character_count(user_list):\n",
        "  no_space = [char for char in user_list if char != ' ']\n",
        "  no_space.sort()\n",
        "  times = {}\n",
        "  for i in no_space:\n",
        "      if i not in times:\n",
        "          times[i] = 1\n",
        "      else:\n",
        "          times[i] +=1\n",
        "  return times\n",
        "\n",
        "print(character_count('smiles'))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tw9wGrJ4t3T0",
        "outputId": "6a4a64b2-feea-43f3-e31b-e120825ff533"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'e': 1, 'i': 1, 'l': 1, 'm': 1, 's': 2}\n"
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
        "! gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko\n",
        "file_path = '/content/P1_data.txt'\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kaJauR9JvMl_",
        "outputId": "3f63b3db-1e5d-40aa-c02d-3f92d9b90320"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko\n",
            "To: /content/P1_data.txt\n",
            "\r  0% 0.00/747 [00:00<?, ?B/s]\r100% 747/747 [00:00<00:00, 2.03MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def count_word(file_path):\n",
        "  counter = {}\n",
        "  file_path = open(file_path, 'r')\n",
        "  file_path = file_path.read().split()\n",
        "  for _ in file_path:\n",
        "    if _ not in counter:\n",
        "      counter[_] = 1\n",
        "    else:\n",
        "      counter[_] += 1\n",
        "  return counter\n",
        "result = count_word(file_path)\n",
        "print(result)\n",
        "print(result['man'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tPM2TnVpwVDF",
        "outputId": "28f472a2-02ca-47ea-bb2c-7a3983a1c0b4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'He': 1, 'who': 3, 'conquers': 1, 'himself': 1, 'is': 3, 'the': 4, 'mightiest': 1, 'warrior': 1, 'Try': 1, 'not': 1, 'to': 3, 'become': 2, 'a': 6, 'man': 6, 'of': 4, 'success': 2, 'but': 1, 'rather': 1, 'value': 1, 'One': 2, 'with': 4, 'courage': 1, 'makes': 1, 'majority': 1, 'secret': 1, 'in': 4, 'life': 2, 'for': 3, 'be': 1, 'ready': 1, 'his': 2, 'opportunity': 1, 'when': 2, 'it': 2, 'comes': 2, 'The': 1, 'successful': 2, 'will': 2, 'profit': 1, 'from': 1, 'mistakes': 1, 'and': 1, 'try': 1, 'again': 1, 'different': 1, 'way': 1, 'A': 1, 'one': 2, 'can': 3, 'lay': 1, 'firm': 1, 'foundation': 1, 'bricks': 1, 'others': 1, 'have': 1, 'thrown': 1, 'at': 1, 'him': 1, 'Success': 1, 'usually': 1, 'those': 1, 'are': 1, 'too': 1, 'busy': 1, 'looking': 1, 'We': 1, 'cannot': 1, 'solve': 1, 'problems': 1, 'kind': 1, 'thinking': 1, 'we': 2, 'employed': 1, 'came': 1, 'up': 1, 'them': 1, 'Just': 1, 'small': 1, 'positive': 1, 'thought': 1, 'morning': 1, 'change': 1, 'your': 1, 'whole': 1, 'day': 1, 'You': 1, 'get': 2, 'everything': 1, 'you': 2, 'want': 2, 'if': 1, 'just': 1, 'help': 1, 'enough': 1, 'other': 1, 'people': 1, 'what': 1, 'they': 1}\n",
            "6\n"
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
        "def levenshtein_distance(token1, token2):\n",
        "  distance_list = [[0 for x in range(len(token2)+1)] for x in range(len(token1)+1)]\n",
        "  for i in range(len(token1)+1):\n",
        "    for j in range(len(token2)+1):\n",
        "        if i == 0:\n",
        "            distance_list[i][j] = j\n",
        "        elif j == 0:\n",
        "            distance_list[i][j] = i\n",
        "        elif token1[i-1] == token2[j-1]:\n",
        "            distance_list[i][j] = distance_list[i-1][j-1]\n",
        "        else:\n",
        "            distance_list[i][j] = 1 + min(distance_list[i][j-1], distance_list[i-1][j], distance_list[i-1][j-1])\n",
        "  return distance_list[len(token1)][len(token2)]\n",
        "print(levenshtein_distance('Hola', 'Hello'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KzYpBv2FzM6w",
        "outputId": "9df0d105-36d4-4e09-f6b2-784dd51d998d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
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
        "def check_the_number(N):\n",
        "  list_of_numbers = []\n",
        "  result = \"\"\n",
        "  for i in range(1, 5):\n",
        "    list_of_numbers.append(i)\n",
        "    if N in list_of_numbers:\n",
        "      results = \"True\"\n",
        "    if N not in list_of_numbers:\n",
        "      results = \"False\"\n",
        "  return results\n",
        "N = 2\n",
        "print(check_the_number(N))"
      ],
      "metadata": {
        "id": "JMe-DWKbq3IQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6d5137c8-3bbd-46dc-c6e7-6ef7ffffa3c1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 6:\n"
      ],
      "metadata": {
        "id": "6k6vNGRV0vG2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def max_and_min(data, max, min) :\n",
        "  result = []\n",
        "  for i in data :\n",
        "    if i < min:\n",
        "      result.append(min)\n",
        "    elif i > max:\n",
        "      result.append(max)\n",
        "    else:\n",
        "      result.append(i)\n",
        "  return result\n",
        "\n",
        "my_list = [10 , 2 , 5 , 0 , 1]\n",
        "max = 2\n",
        "min = 1\n",
        "print(max_and_min(max = max, min = min, data = my_list))"
      ],
      "metadata": {
        "id": "EH5Qj6LQ004Z",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b4eee064-8188-4fff-c7d1-07aeee54229e"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 2, 2, 1, 1]\n"
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
        "def extend_list(x , y):\n",
        "  x.extend(y)\n",
        "  return x\n",
        "\n",
        "list_num1 = [1 , 2]\n",
        "list_num2 = [3 , 4]\n",
        "list_num3 = [0 , 0]\n",
        "print(extend_list(list_num1,extend_list(list_num2, list_num3)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AocQN8paXXZq",
        "outputId": "11ec7fd0-aece-4c21-d23c-2281212d4d18"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 0, 0]\n"
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
        "def min_number(n) :\n",
        "  min = n[0]\n",
        "  for _ in n:\n",
        "    if _ < min:\n",
        "      min = _\n",
        "  return min\n",
        "\n",
        "my_list = [1 , 2 , 3 , -1]\n",
        "print(min_number(my_list))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xUuPol6OYgQX",
        "outputId": "56e7cdc3-7fb6-4b3a-e211-b4bf6e29ab85"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-1\n"
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
        "def max_number(n):\n",
        "  max = n[0]\n",
        "  for _ in n:\n",
        "    if _ > max:\n",
        "      max = _\n",
        "  return max\n",
        "\n",
        "my_list = [1 , 9 , 9 , 0]\n",
        "print(max_number(my_list))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LyrKZ5V5Y9X6",
        "outputId": "55ba7c76-4441-4bbb-9807-b5ca5712ab2e"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9\n"
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
        "def find_number(integers, number = 1) :\n",
        "  result = []\n",
        "  for i in integers:\n",
        "    if i == number:\n",
        "      return True\n",
        "  if len(result) == 0:\n",
        "    return False\n",
        "\n",
        "my_list = [1 , 2 , 3 , 4]\n",
        "print(find_number(my_list, 2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MB8uXg_OZZrX",
        "outputId": "13e0a56e-b1f1-450d-8e89-460b69fa923a"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
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
        "def average_number(list_nums = [0 , 1 , 2]):\n",
        "  var = 0\n",
        "  for i in list_nums:\n",
        "    var += i\n",
        "  return var/len(list_nums)\n",
        "print(average_number())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rOaRiezdao02",
        "outputId": "8c7de01a-b0ee-454a-e8d4-5d5cecb7323b"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.0\n"
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
        "def divide_three(data):\n",
        "  var = []\n",
        "  for i in data:\n",
        "    if i%3 == 0:\n",
        "      var.append(i)\n",
        "  return var\n",
        "\n",
        "my_list = [1, 2, 3, 5, 6]\n",
        "print(divide_three(my_list))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uXDTzGG7be4L",
        "outputId": "e19d2268-b49d-4eb7-f2b5-248881f33d9f"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[3, 6]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 13"
      ],
      "metadata": {
        "id": "yCjT9gjWari9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def factorial(y):\n",
        "  var = 1\n",
        "  while y > 1:\n",
        "    i = y\n",
        "    y -= 1\n",
        "    var *= i\n",
        "  return var\n",
        "print(factorial(4))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fw_zuchKatUe",
        "outputId": "056896bd-d712-4e63-b938-8c3cb4085a55"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "24\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 14"
      ],
      "metadata": {
        "id": "w5nflhcYatoF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def reverse_string(x):\n",
        "  return x[::-1]\n",
        "print(reverse_string('apricot'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5CjKfdpgavp_",
        "outputId": "32e40486-ebb7-414f-a52b-9055e985f406"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "tocirpa\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 15"
      ],
      "metadata": {
        "id": "Xvl-WYdzavun"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def positive_and_negative(x):\n",
        "  if x > 0:\n",
        "    return 'T'\n",
        "  else:\n",
        "    return 'N'\n",
        "\n",
        "def check_the_number(N):\n",
        "  res = [positive_and_negative(x) for x in N]\n",
        "  return res\n",
        "\n",
        "N = [2, 3, 5, -1]\n",
        "print(check_the_number(N))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fb-s10Qraxgz",
        "outputId": "094df650-29ff-48ea-8cfd-65fd8c9abb17"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['T', 'T', 'T', 'N']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 16"
      ],
      "metadata": {
        "id": "vQ5_x1mkeov-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_the_same(x, data):\n",
        "  for i in data:\n",
        "    if x == i:\n",
        "      return 0\n",
        "  return 1\n",
        "\n",
        "def check_the_number(data):\n",
        "  res = []\n",
        "  for j in data:\n",
        "    if remove_the_same(j, res):\n",
        "      res.append(j)\n",
        "  return res\n",
        "\n",
        "lst = [9 , 9 , 8 , 1 , 1]\n",
        "print(check_the_number(lst))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lyixzSdKeriN",
        "outputId": "d650ce48-30d7-41ea-ea23-9240c338efeb"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[9, 8, 1]\n"
          ]
        }
      ]
    }
  ]
}
