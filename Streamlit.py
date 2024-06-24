{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOttmWCSb8JZUj7hxapGIPJ",
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
        "<a href=\"https://colab.research.google.com/github/Ducanhngo/AIO_2024_087_AnhDuc/blob/feature%2Fexercise/Streamlit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Prepare![image_2024-06-24_140707540.png](data:image/png;base64,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)"
      ],
      "metadata": {
        "id": "9MuN2rGY66vh"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "1Mj2hgQIZuUE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e1949e52-0291-46b8-f016-408d45689999"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount(\"/content/drive\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "FMZX8gfI6zP1",
        "outputId": "40a39aff-e2c3-4839-d840-fdb11692e47a"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.36.0-py2.py3-none-any.whl (8.6 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.6/8.6 MB\u001b[0m \u001b[31m22.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.3)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.25.2)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.0.3)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.31.0)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.4.1)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m7.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m39.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<5,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-4.0.1-py3-none-manylinux2014_x86_64.whl (83 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m83.0/83.0 kB\u001b[0m \u001b[31m3.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2023.4)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.6.2)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.1)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Installing collected packages: watchdog, smmap, pydeck, gitdb, gitpython, streamlit\n",
            "Successfully installed gitdb-4.0.11 gitpython-3.1.43 pydeck-0.9.1 smmap-5.0.1 streamlit-1.36.0 watchdog-4.0.1\n"
          ]
        }
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
        "import streamlit as st\n",
        "\n",
        "st.text(\"Hello world\")"
      ],
      "metadata": {
        "id": "l9kfAbzl-BC9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "444d94a1-8ae7-4125-c7f4-9b55a5d86c8d"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py"
      ],
      "metadata": {
        "id": "RYkX-kkoGzdt",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a3cb6330-a6ae-42d4-d6e5-b536109f2d3d"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.199.49.114:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n"
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
        "colors = [\"Green\", \"Yellow\", \"Red\", \"Blue\"]\n",
        "default_colors = [\"Yellow\", \"Red\"]\n",
        "options = st.multiselect(\"Your favorite colors:\",\n",
        "                         colors, default=default_colors)\n",
        "st.write(\"You selected:\", options)"
      ],
      "metadata": {
        "id": "vcMYkDfbGzg-"
      },
      "execution_count": 17,
      "outputs": []
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
        "st.text_input(\"User:\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "MjsE15R_JYVz",
        "outputId": "a4218444-d59b-4e0f-a6c7-805def632f79"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-06-24 06:48:15.173 Session state does not function when running a script without `streamlit run`\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "''"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 18
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
        "st.image(image_path, caption='A cat', width='RGB', channels='BGR')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "id": "nfukBziFGr_r",
        "outputId": "ab9b8d60-75ae-4d89-9032-325589a96a6e"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'image_path' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-20-bd46678c8f61>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mimage\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimage_path\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcaption\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'A cat'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwidth\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'RGB'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mchannels\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'BGR'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'image_path' is not defined"
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
        "def levenshtein_distance(token1, token2):\n",
        "    distances = [[0]*(len(token2)+1) for _ in range(len(token1)+1)]\n",
        "\n",
        "    for t1 in range(len(token1) + 1):\n",
        "        distances[t1][0] = t1\n",
        "\n",
        "    for t2 in range(len(token2) + 1):\n",
        "        distances[0][t2] = t2\n",
        "\n",
        "    a = 0\n",
        "    b = 0\n",
        "    c = 0\n",
        "\n",
        "    for t1 in range(1, len(token1) + 1):\n",
        "        for t2 in range(1, len(token2) + 1):\n",
        "            if (token1[t1-1] == token2[t2-1]):\n",
        "                distances[t1][t2] = distances[t1 - 1][t2 - 1]\n",
        "            else:\n",
        "                a = distances[t1][t2 - 1]\n",
        "                b = distances[t1 - 1][t2]\n",
        "                c = distances[t1 - 1][t2 - 1]\n",
        "\n",
        "                if (a <= b and a <= c):\n",
        "                    distances[t1][t2] = a + 1\n",
        "                elif (b <= a and b <= c):\n",
        "                    distances[t1][t2] = b + 1\n",
        "                else:\n",
        "                    distances[t1][t2] = c + 1\n",
        "\n",
        "    return distances[len(token1)][len(token2)]\n",
        "print(levenshtein_distance(\"elmets\", \"elements\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jc5EM3pKJJsQ",
        "outputId": "f2333903-0d99-422c-c9f7-1bc493630d2b"
      },
      "execution_count": 22,
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
        "#Question 6:"
      ],
      "metadata": {
        "id": "3g-DpnwmDevv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "st.session_state"
      ],
      "metadata": {
        "id": "avUCxVO1EjwQ"
      },
      "execution_count": null,
      "outputs": []
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
        "import streamlit as st\n",
        "\n",
        "with st.form(\"my_form\"):\n",
        "    col1, col2 = st.columns(2)\n",
        "    f_name = col1.text_input('First Name')\n",
        "    l_name = col2.text_input('Last Name')\n",
        "    submitted = st.form_submit_button(\"Submit\")\n",
        "\n",
        "    if submitted:\n",
        "        st.write(\"First Name:\", f_name, \" - Last Name:\", l_name)"
      ],
      "metadata": {
        "id": "La9wj8tmJeXV"
      },
      "execution_count": 23,
      "outputs": []
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
        "uploaded_files = st.file_uploader(\"Choose files\", accept_multiple_files=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rqhj99BtN4dO",
        "outputId": "42b3baff-fae9-4092-8968-9379505bfd79"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.07558372781130615 0.1137051486131346 0.04069766993531071\n"
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
        "st.slider()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s-8PWMbAODMv",
        "outputId": "cfabe3f6-5b8e-4283-f35d-4c0ea0a0d432"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "predicted sales is 7.616725552375692 \n"
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
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "v7WkjdwHEdsu"
      }
    }
  ]
}