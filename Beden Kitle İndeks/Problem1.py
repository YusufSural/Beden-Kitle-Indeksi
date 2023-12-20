{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "initial_id",
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "boy = float(input(\"Boyunuzu giriniz: \"))\n",
    "kilo = float(input(\"Kilonuzu giriniz: \"))\n",
    "\n",
    "hesap = kilo / (boy * boy)\n",
    "\n",
    "if hesap < 18.5:\n",
    "    print(f\"BKİ sonucu: {hesap}\",\"Zayıfsınız.\")\n",
    "elif hesap > 18.5 and hesap <= 25:\n",
    "    print(f\"BKİ sonucu: {hesap}\",\"Normal.\")\n",
    "elif hesap > 25 and hesap <= 30:\n",
    "    print(f\"BKİ sonucu: {hesap}\",\"Fazla kilolu.\")\n",
    "else:\n",
    "    print(f\"BKİ sonucu: {hesap}\",\"Obez.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
