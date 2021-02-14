# import modules
import os
import json
import argparse
import pandas as pd


def main():
    # perform argument parsing
    parser = argparse.ArgumentParser(description='Radiology data analysis')
    parser.add_argument('--spotters', type=str, required=True,
                        help='Spotters list for analysis')
    parser.add_argument('--image-dir', type=str, required=True,
                        help='Images directory for downloading images')
    parser.add_argument('--output-dir', type=str, required=True,
                        help='Output directory for json files')
    args = parser.parse_args()

    # load the spotters master list
    spotter_df = pd.read_csv(args.spotters)

    # generate a list of google queries to be generated
    spotter_queries = spotter_df['Condition']
    spotter_answers = spotter_df['Answer']
    keyboard()

    # generate quiz json based on queries
    result = {
        'briefName': 'radiology-spotters',
        'title': 'Radiology Spotters',
        'config': {
            'randomizeQuestionSequence': True,
            'autoSubmit': False,
            'percentGreatJob': 60,
        },
        'questions': []
    }

    image_dir = 'images'
    question_id = 0
    for query, answer in zip(spotter_queries, spotter_answers):
        images_dir = os.path.join(image_dir, query)
        images_dir = images_dir.strip().replace(' ', '_')
        image_files = os.listdir(images_dir)
        for image_file in image_files:
            question_dict = {
                'id': question_id,
                'question': 'What is the condition in this image?',
                'pictureQuestion': os.path.join(images_dir, image_file),
                'type': 'pictureQuestionShortAnswer',
                'correctAnswerArray': [
                    answer.lower(),
                    answer,
                    answer.lower().capitalize()
                ]
            }
            result['questions'].append(question_dict)

    result_path = os.path.join(args.output_dir, 'radiology-spotters.json')
    with open(result_path, 'w') as f:
        json.dump(result, f, indent=4)


if __name__=='__main__':
    main()
