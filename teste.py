{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN0k0Zerht7xebHMBqe/fQu",
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
        "<a href=\"https://colab.research.google.com/github/daniloasdotcom/ControllingClient/blob/main/teste.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "id": "wvazbuRqGNR5",
        "outputId": "fd95514e-7bf2-4084-baf6-d8f89868f43d"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.12.2-py2.py3-none-any.whl (9.1 MB)\n",
            "\u001b[K     |████████████████████████████████| 9.1 MB 25.4 MB/s \n",
            "\u001b[?25hRequirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.12.0)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.4)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.17.3)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.5.1)\n",
            "Collecting semver\n",
            "  Downloading semver-2.13.0-py2.py3-none-any.whl (12 kB)\n",
            "Collecting rich>=10.11.0\n",
            "  Downloading rich-12.5.1-py3-none-any.whl (235 kB)\n",
            "\u001b[K     |████████████████████████████████| 235 kB 56.1 MB/s \n",
            "\u001b[?25hRequirement already satisfied: toml in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.10.2)\n",
            "Collecting pydeck>=0.1.dev5\n",
            "  Downloading pydeck-0.8.0b3-py2.py3-none-any.whl (4.7 MB)\n",
            "\u001b[K     |████████████████████████████████| 4.7 MB 51.3 MB/s \n",
            "\u001b[?25hRequirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.1.1)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.23.0)\n",
            "Collecting pympler>=0.9\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[K     |████████████████████████████████| 164 kB 71.1 MB/s \n",
            "\u001b[?25hCollecting blinker>=1.0.0\n",
            "  Downloading blinker-1.5-py2.py3-none-any.whl (12 kB)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (5.1.1)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.3.5)\n",
            "Collecting watchdog\n",
            "  Downloading watchdog-2.1.9-py3-none-manylinux2014_x86_64.whl (78 kB)\n",
            "\u001b[K     |████████████████████████████████| 78 kB 7.6 MB/s \n",
            "\u001b[?25hRequirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.0)\n",
            "Collecting gitpython!=3.1.19\n",
            "  Downloading GitPython-3.1.27-py3-none-any.whl (181 kB)\n",
            "\u001b[K     |████████████████████████████████| 181 kB 70.4 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (6.0.1)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.8.2)\n",
            "Collecting validators>=0.2\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.3)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.21.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.12.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Collecting gitdb<5,>=4.0.1\n",
            "  Downloading gitdb-4.0.9-py3-none-any.whl (63 kB)\n",
            "\u001b[K     |████████████████████████████████| 63 kB 1.7 MB/s \n",
            "\u001b[?25hCollecting smmap<6,>=3.0.1\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=1.4->streamlit) (3.8.1)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (5.9.0)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (22.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.1)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging>=14.1->streamlit) (3.0.9)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.21.0->streamlit) (2022.2.1)\n",
            "Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.7/dist-packages (from protobuf<4,>=3.12->streamlit) (1.15.0)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests>=2.4->streamlit) (1.24.3)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests>=2.4->streamlit) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests>=2.4->streamlit) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests>=2.4->streamlit) (2022.6.15)\n",
            "Collecting commonmark<0.10.0,>=0.9.0\n",
            "  Downloading commonmark-0.9.1-py2.py3-none-any.whl (51 kB)\n",
            "\u001b[K     |████████████████████████████████| 51 kB 5.3 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pygments<3.0.0,>=2.6.0 in /usr/local/lib/python3.7/dist-packages (from rich>=10.11.0->streamlit) (2.6.1)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.7/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19582 sha256=46b177e537fe680bb4610f878fec57cb072406a10748eaccff284c26fd81059d\n",
            "  Stored in directory: /root/.cache/pip/wheels/5f/55/ab/36a76989f7f88d9ca7b1f68da6d94252bb6a8d6ad4f18e04e9\n",
            "Successfully built validators\n",
            "Installing collected packages: smmap, gitdb, commonmark, watchdog, validators, semver, rich, pympler, pydeck, gitpython, blinker, streamlit\n",
            "Successfully installed blinker-1.5 commonmark-0.9.1 gitdb-4.0.9 gitpython-3.1.27 pydeck-0.8.0b3 pympler-1.0.1 rich-12.5.1 semver-2.13.0 smmap-5.0.0 streamlit-1.12.2 validators-0.20.0 watchdog-2.1.9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "voGrrfeFGbau"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SRfCsD-0D4XG",
        "outputId": "b18b1962-5243-43bf-fcd8-4581d45d1cda"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:numexpr.utils:NumExpr defaulting to 2 threads.\n",
            "2022-09-21 22:09:27.848 INFO    numexpr.utils: NumExpr defaulting to 2 threads.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.title('Uber pickups in NYC')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fZVaQScaGBYX",
        "outputId": "5176a7b5-9a9c-431f-c5dd-81ec3c0cd662"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    }
  ]
}