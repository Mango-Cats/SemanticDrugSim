// PubMed XML to Text Corpus Converter
// By: Zhean Ganituen (zrygan)
// On: August 2025
package main

import (
	"encoding/xml"
	"fmt"
	"io"
	"os"
	"path/filepath"
)

type PubmedArticleSet struct {
	Articles []PubmedArticle `xml:"PubmedArticle"`
}

type PubmedArticle struct {
	MedlineCitation MedlineCitation `xml:"MedlineCitation"`
}

type MedlineCitation struct {
	Article Article `xml:"Article"`
}

type Article struct {
	Abstract Abstract `xml:"Abstract"`
}

type Abstract struct {
	Texts []string `xml:"AbstractText"`
}

func main() {
	// Directory containing XML files
	xmlDir := "corpus/PubMedBaselineRepository"
	outputFile := "pubmed_corpus.txt"

	out, err := os.Create(outputFile)
	if err != nil {
		panic(err)
	}
	defer out.Close()

	files, err := filepath.Glob(filepath.Join(xmlDir, "*.xml"))
	if err != nil {
		panic(err)
	}

	for _, file := range files {
		fmt.Println("Processing:", file)
		f, err := os.Open(file)
		if err != nil {
			fmt.Println("Error opening file:", file, err)
			continue
		}

		decoder := xml.NewDecoder(f)
		for {
			tok, err := decoder.Token()
			if err != nil {
				if err == io.EOF {
					break
				}
				fmt.Println("Error decoding XML:", err)
				break
			}

			switch se := tok.(type) {
			case xml.StartElement:
				if se.Name.Local == "PubmedArticle" {
					var article PubmedArticle
					if err := decoder.DecodeElement(&article, &se); err != nil {
						fmt.Println("Decode error:", err)
						continue
					}
					// Combine all AbstractText nodes into one line
					if len(article.MedlineCitation.Article.Abstract.Texts) > 0 {
						abstract := ""
						for _, t := range article.MedlineCitation.Article.Abstract.Texts {
							abstract += t + " "
						}
						_, _ = out.WriteString(abstract + "\n")
					}
				}
			}
		}
		f.Close()
	}

	fmt.Println("Done! Corpus saved to", outputFile)
}
