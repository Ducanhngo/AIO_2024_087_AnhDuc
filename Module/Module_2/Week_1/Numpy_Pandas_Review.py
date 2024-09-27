{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOon3KIrJlKPNnMG8o2fUVB",
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
        "<a href=\"https://colab.research.google.com/github/Ducanhngo/AIO_2024_087_AnhDuc/blob/feature%2Fexercise/Numpy_Pandas_Review.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 1:"
      ],
      "metadata": {
        "id": "_ULSxC3b6zdB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.arange(0,10,1)\n",
        "print(arr)"
      ],
      "metadata": {
        "id": "l9kfAbzl-BC9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e02a49a1-ba80-4863-a4c9-b69a56b5784a"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0 1 2 3 4 5 6 7 8 9]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 2:"
      ],
      "metadata": {
        "id": "KWzFwcnp-QWy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.ones((3,3)) > 0\n",
        "print(arr)"
      ],
      "metadata": {
        "id": "vcMYkDfbGzg-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b419cc66-3ce8-4e4d-d828-7b6410d77f9b"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ True  True  True]\n",
            " [ True  True  True]\n",
            " [ True  True  True]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.ones((3,3), dtype = bool)\n",
        "print(arr)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QauxCB28lb4F",
        "outputId": "51da64ae-4664-4d75-fce0-a8cd7fea1e96"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ True  True  True]\n",
            " [ True  True  True]\n",
            " [ True  True  True]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.full((3,3), fill_value = True, dtype = bool)\n",
        "print(arr)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X0DCrhdTlcFC",
        "outputId": "f9d7ba77-d652-4d73-fbb7-4e46e9615c57"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ True  True  True]\n",
            " [ True  True  True]\n",
            " [ True  True  True]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 3:"
      ],
      "metadata": {
        "id": "12D_fNePAKYP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.arange(0,10)\n",
        "print(arr[arr%2 == 1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MjsE15R_JYVz",
        "outputId": "19a01092-d2c3-4eec-b018-1e102e186516"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 3 5 7 9]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 4:"
      ],
      "metadata": {
        "id": "IpWEjypvAN_d"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.arange(0,10)\n",
        "arr[arr%2 == 1] = -1\n",
        "print(arr)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nfukBziFGr_r",
        "outputId": "38a993f1-5d4a-423e-faa9-6ea4f1d667f3"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[ 0 -1  2 -1  4 -1  6 -1  8 -1]\n"
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
        "id": "efUI2_qSCaeK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.arange(10)\n",
        "arr_2d = arr.reshape(2, -1)\n",
        "print(arr_2d)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jc5EM3pKJJsQ",
        "outputId": "0f979a90-c3fb-420a-f2fd-76a8a34d2091"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0 1 2 3 4]\n",
            " [5 6 7 8 9]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 6:"
      ],
      "metadata": {
        "id": "3g-DpnwmDevv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr1= np.arange(10).reshape(2, -1)\n",
        "arr2 = np.repeat(1,10).reshape(2,-1)\n",
        "c = np.concatenate([arr1, arr2],axis = 0)\n",
        "print(\"Result: \\n\", c )"
      ],
      "metadata": {
        "id": "avUCxVO1EjwQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "91f92ae5-a3dc-448e-cd23-13c4fa6f15f4"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result: \n",
            " [[0 1 2 3 4]\n",
            " [5 6 7 8 9]\n",
            " [1 1 1 1 1]\n",
            " [1 1 1 1 1]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 7:"
      ],
      "metadata": {
        "id": "ko78QUrFDjHg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr1= np.arange(10).reshape(2, -1)\n",
        "arr2 = np.repeat(1,10).reshape(2,-1)\n",
        "c = np.concatenate([arr1, arr2],axis = 1)\n",
        "print(\"C = \", c )"
      ],
      "metadata": {
        "id": "La9wj8tmJeXV",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "05f9b46f-053b-434b-d603-b9413ab90772"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "C =  [[0 1 2 3 4 1 1 1 1 1]\n",
            " [5 6 7 8 9 1 1 1 1 1]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 8:"
      ],
      "metadata": {
        "id": "xyciU4DgDpdq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.array([1,2,3])\n",
        "print(np.repeat(arr,3))\n",
        "print(np.tile(arr,3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rqhj99BtN4dO",
        "outputId": "793d1c28-86b5-4033-8430-12dadb7a78d6"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 1 1 2 2 2 3 3 3]\n",
            "[1 2 3 1 2 3 1 2 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 9:"
      ],
      "metadata": {
        "id": "WAiSx7BfDvFs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr = np.array([2, 6, 1, 9, 10, 3, 27])\n",
        "index = np.where((arr >=5 ) & (arr <= 10))\n",
        "print(\"Result:\", arr[index] )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s-8PWMbAODMv",
        "outputId": "bce7a7ac-0d1d-4ddd-8c5b-e5b69222d6e4"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result: [ 6  9 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 10:"
      ],
      "metadata": {
        "id": "aaJYgo_FDxZY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "def maxx(x, y):\n",
        "    if x >= y:\n",
        "        return x\n",
        "    else:\n",
        "        return y\n",
        "\n",
        "a = np.array([5, 7, 9, 8, 6, 4, 5])\n",
        "b = np.array([6, 3, 4, 8, 9, 7, 1])\n",
        "\n",
        "pair_max = np.vectorize(maxx, otypes = [float])\n",
        "print(pair_max(a, b))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n3VMpPWSqw8U",
        "outputId": "f22f73fc-648c-4f55-f076-cc749177cded"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[6. 7. 9. 8. 9. 7. 5.]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 11:"
      ],
      "metadata": {
        "id": "3pJYcDEBqyQ3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "a = np.array([5, 7, 9, 8, 6, 4, 5])\n",
        "b = np.array([6, 3, 4, 8, 9, 7, 1])\n",
        "\n",
        "print(\"Result\", np.where(a< b, b, a))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1UlL4LGpqyc6",
        "outputId": "34a37645-9d8e-4606-92b4-54868a58092e"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result [6 7 9 8 9 7 5]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 12:"
      ],
      "metadata": {
        "id": "1O9NHEtEqynX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!gdown '1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "erFGOzMBxy-V",
        "outputId": "f98a7212-bc3f-4678-be4f-9118bea89299"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB\n",
            "To: /content/dog.jpeg\n",
            "\r  0% 0.00/33.7k [00:00<?, ?B/s]\r100% 33.7k/33.7k [00:00<00:00, 59.5MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.image as mpimg\n",
        "img = mpimg.imread('dog.jpeg')\n",
        "gray_img_01 = np.zeros((img.shape[0], img.shape[1]), dtype = np.float32)\n",
        "for i in range(img.shape[0]):\n",
        "  for j in range(img.shape[1]):\n",
        "    r, g, b = img[i, j].astype(np.float32)\n",
        "    min_val = min(r, g, b)\n",
        "    max_val = max(r, g, b)\n",
        "    gray_img_01[i, j] = (min_val + max_val) / 2\n",
        "print(gray_img_01[0, 0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tmYAixLyqyyL",
        "outputId": "819414dd-1604-46b1-f6fe-8d582780dc35"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "102.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 13:"
      ],
      "metadata": {
        "id": "6wSa_6VEqy9P"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.image as mpimg\n",
        "img = mpimg.imread('dog.jpeg')\n",
        "gray_img_02 = np.zeros((img.shape[0], img.shape[1]), dtype = np.float32)\n",
        "for i in range(img.shape[0]):\n",
        "  for j in range(img.shape[1]):\n",
        "    r, g, b = img[i, j].astype(np.float32)\n",
        "    gray_img_02[i, j] = (r + g + b)/ 3\n",
        "print(gray_img_02[0, 0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xYf9cyvmqzGb",
        "outputId": "65c7c5bf-7113-4cd5-f0bf-1df49ff91ee4"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "107.666664\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 14:"
      ],
      "metadata": {
        "id": "gFOrgj1UqzRT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.image as mpimg\n",
        "img = mpimg.imread('dog.jpeg')\n",
        "gray_img_03 = np.zeros((img.shape[0], img.shape[1]), dtype = np.float32)\n",
        "for i in range(img.shape[0]):\n",
        "  for j in range(img.shape[1]):\n",
        "    r, g, b = img[i, j].astype(np.float32)\n",
        "    gray_img_03[i, j] = 0.21*r + 0.72*g + 0.07*b\n",
        "print(gray_img_03[0, 0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zH5iaQbzqzbi",
        "outputId": "cd6a713f-742d-40f4-c688-0df16a720aa4"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "126.23\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 15:"
      ],
      "metadata": {
        "id": "7KRrFRqJqzlg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!gdown '1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "okgREmdUqzup",
        "outputId": "b50b196b-2e9d-4af7-a267-6c8ce477bf81"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq\n",
            "To: /content/advertising.csv\n",
            "\r  0% 0.00/4.06k [00:00<?, ?B/s]\r100% 4.06k/4.06k [00:00<00:00, 13.1MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('/content/advertising.csv')\n",
        "data = df.to_numpy()\n",
        "max_sales = df['Sales'].max()\n",
        "max_sales_index = df['Sales'].idxmax()\n",
        "print('Index:', max_sales_index, end = ', ')\n",
        "print(\"Max:\", max_sales)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2xgXjGKwNZ19",
        "outputId": "a4f41b9d-c90b-4151-b7da-894b919b2246"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index: 175, Max: 27.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 16:"
      ],
      "metadata": {
        "id": "-P3mcQFOqz6Z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('/content/advertising.csv')\n",
        "data = df.to_numpy()\n",
        "average_TV = df['TV'].mean()\n",
        "print('Average TV:', average_TV)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B3XJ_5A3q0Ds",
        "outputId": "837d9de9-623b-4f58-f02f-982218b473ba"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Average TV: 147.0425\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 17:"
      ],
      "metadata": {
        "id": "Eykk9Jy1vqUG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('/content/advertising.csv')\n",
        "data = df.to_numpy()\n",
        "count_sales_gte_20 = (df.Sales >= 20).sum()\n",
        "print(count_sales_gte_20)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eB6GNuxYvqmK",
        "outputId": "b6bb83c1-6224-45a0-dfb4-4ad1e0363c16"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "40\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 18:"
      ],
      "metadata": {
        "id": "PAECmH8Bvq03"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('/content/advertising.csv')\n",
        "data = df.to_numpy()\n",
        "filtered_df = df[df['Sales'] >= 15]\n",
        "mean_radio = filtered_df['Radio'].mean()\n",
        "print('Mean Radio:', mean_radio)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l__W_YGGvq-N",
        "outputId": "f7c6e488-fe87-4311-a783-881d9932bf4d"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mean Radio: 26.22293577981651\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 19:"
      ],
      "metadata": {
        "id": "C5Fx_ZsyvrK7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('/content/advertising.csv')\n",
        "data = df.to_numpy()\n",
        "filtered_df = df[df['Newspaper'] > df['Newspaper'].mean()]\n",
        "sum_sales = filtered_df['Sales'].sum()\n",
        "print('Sum Sales:', sum_sales)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0Cj9tV4EvrX-",
        "outputId": "db40d291-79f6-4628-f33f-fe9c1a5d384e"
      },
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sum Sales: 1405.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 20:"
      ],
      "metadata": {
        "id": "JkiNylYzvrmG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('/content/advertising.csv')\n",
        "data = df.to_numpy()\n",
        "mean_sales = df['Sales'].mean()\n",
        "df['Asset Sales'] = np.where(df['Sales'] > mean_sales, 'Good', np.where(df['Sales'] < mean_sales, 'Bad', 'Average'))\n",
        "scores = df['Asset Sales'].to_numpy()\n",
        "print('Asset Sales:', scores[7:10])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X-_Wa1xYvrt6",
        "outputId": "23a7c93d-ccaf-4fe9-b60d-424d40b7f6be"
      },
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Asset Sales: ['Bad' 'Bad' 'Good']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Question 21:"
      ],
      "metadata": {
        "id": "N6jtfT0CR9TQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('/content/advertising.csv')\n",
        "data = df.to_numpy()\n",
        "mean_sales = df['Sales'].mean()\n",
        "nearest_mean_sales = np.abs(df['Sales'] - mean_sales).idxmin()\n",
        "nearest_value = df.loc[nearest_mean_sales, 'Sales']\n",
        "df['Asset Sales'] = np.where(df['Sales'] > nearest_value, 'Good', np.where(df['Sales'] < nearest_value, 'Bad', 'Average'))\n",
        "scores = df['Asset Sales'].to_numpy()\n",
        "print('Asset Sales:', scores[7:10])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jGnPfShEaLR2",
        "outputId": "c4dd0f0b-925f-4ae2-d500-a2f15e6e80c6"
      },
      "execution_count": 87,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Asset Sales: ['Bad' 'Bad' 'Good']\n"
          ]
        }
      ]
    }
  ]
}