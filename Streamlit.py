{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPpFPwu7iODY3VTD3KoQC2B",
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