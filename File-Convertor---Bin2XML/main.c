#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct _element
{
    char name[64];            // utf-16
    char surname[32];         // utf-8
    char gender;
    char email[32];
    char phoneNumber[16];
    char address[32];
    char levelOfEducation[8];
    unsigned int incomeLevel; // given little-endian
    unsigned int expenditure; // given big-endian
    char currencyUnit[16];
    char currentMood[32];
    float height;
    unsigned int weight;
};
typedef struct _element element;

unsigned int convertOrder(unsigned int toBeConverted)
{
    int num = toBeConverted;
    int b0,b1,b2,b3;
    int res;

    b0 = (num & 0x000000ff) << 24u;
    b1 = (num & 0x0000ff00) << 8u;
    b2 = (num & 0x00ff0000) >> 8u;
    b3 = (num & 0xff000000) >> 24u;

    res = b0 | b1 | b2 | b3;

    return res; 
}

void createXML(FILE *fb, element XMLelement, element tag)
{
    fprintf(fb, "\t\t<%s>%s</%s>\n",tag.name, XMLelement.name, tag.name);
    fprintf(fb, "\t\t<%s>%s</%s>\n",tag.surname, XMLelement.surname, tag.surname);
    char gender[10] = "gender";
    fprintf(fb, "\t\t<%s>%c</%s>\n", gender, XMLelement.gender, gender);
    fprintf(fb, "\t\t<%s>%s</%s>\n", tag.email, XMLelement.email, tag.email);
    fprintf(fb, "\t\t<%s>%s</%s>\n", tag.phoneNumber, XMLelement.phoneNumber, tag.phoneNumber);
    fprintf(fb, "\t\t<%s>%s</%s>\n", tag.address, XMLelement.address, tag.address);
    char levelOfEducation[20] = "level_of_education";
    fprintf(fb, "\t\t<%s>%s</%s>\n", levelOfEducation, XMLelement.levelOfEducation, levelOfEducation);
    fprintf(fb, "\t\t<%s>%s</%s>\n",tag.currencyUnit, XMLelement.currencyUnit, tag.currencyUnit);
    char height[10] = "height";
    fprintf(fb, "\t\t<%s>%.2f</%s>\n", height, XMLelement.height, height);
    char weight[10] = "weight";
    fprintf(fb, "\t\t<%s>%u</%s>\n", weight, XMLelement.weight, weight);
}

void Bin2XML(char inputfile[], char outputfile[])
{
	char name[50] = "";
	element person;
    element tag;
    FILE *fp;
    fp = fopen(inputfile,"r");
    if(fp == NULL)
    {
        printf("File could not be opened!");
        exit(1);
    }
    size_t n = fread(&tag.name, sizeof(element), 1, fp);

    size_t p;
    FILE *fb = fopen(outputfile, "w");
    fprintf(fb, "<?xml version = \"1.0\" encoding = \"utf-8\"?>\n");
    fprintf(fb, "<records>\n");
    int id = 1;
    int i;
    while(p = fread(&person.name, sizeof(element), 1, fp) > 0)
    {
        if(strcmp(person.name, "") != 0)
        {
		    i = 0;
		    strcpy(name,"");
		    while(person.name[i] != -16 && i < strlen(person.name)){
				name[i] = person.name[i];
		    	i++;
			}
			name[i] = '\0';
			strcpy(person.name, "");
			strcpy(person.name, name);
		    unsigned int bigEndianExpenditure = person.expenditure;
            person.expenditure = convertOrder(person.expenditure);
            unsigned int bigEndianIncomeLevel = convertOrder(person.incomeLevel);
            fprintf(fb, "\t<row id=\"%d\">\n", id);
            createXML(fb, person, tag);
            id++;
            fprintf(fb, "\t</row>\n");  
        }
    }
    fprintf(fb, "</records>");
    fclose(fp);
    fclose(fb);
}

int main(int arg , char *argS[])
{

    if(arg == 3)
    {
        Bin2XML(argS[1], argS[2]);
    }
    else
    {
        printf("When running the program, please run as: Assignment1.exe records.dat records.xml");
    }

    return 0;
}
