"""Main entry point for the demo generator"""

from demodata.scripts import patient as p
from demodata.scripts import facility as f
import demodata.util as u
import click


@click.group()
@click.option('--output', default='STDOUT', help='location of output')
@click.pass_context
def cli(ctx, output):
    """Main entry point to the app"""
    ctx.obj = {'output': output}


@click.command()
@click.pass_context
@click.option('--count', default=1, help='number of patients')
@click.option('--sql_out', default=True, help='sql or regular output')
def patients(ctx, count, sql_out):
    """Generate patient data"""
    patient = p.generate_patients(count)
    sql = u.generate_sql('patient_data', patient)

    # @todo Figure out a way to handle the --output option, probably a function called post_process()
    click.echo(sql) if sql_out == True else click.echo(patient)


@click.command()
@click.pass_context
@click.option('--count', default=1, help='number of facilities')
@click.option('--sql_out', default=True, help='sql or regular output')
def facilities(ctx, count, sql_out):
    """Generate faciliity data"""
    facility = f.generate_facility(count)
    sql = u.generate_sql('facility', facility)

    # @todo Figure out a way to handle the --output option, probably a function called post_process()
    click.echo(sql) if sql_out == True else click.echo(facility)

@click.command()
@click.pass_context
@click.option('--filename', default='./dataexport/patient_data.csv', help='filename for output')
@click.option('--count', default=10000, help='number of patients to generate')
def patientsfileout(ctx, filename, count):
    """Generate patient data and output to file"""
    p.generate_patients_txt(filename, count)


cli.add_command(patients)
cli.add_command(facilities)
cli.add_command(patientsfileout)
